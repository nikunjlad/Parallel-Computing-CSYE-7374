from xgboost import XGBClassifier
import time, warnings, random
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV, StratifiedKFold
import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore")   # filter out unnecessary warnings


class Part3:

    def __init__(self, filename, procs, folds, split):
        self.filename = filename
        self.procs = procs
        self.folds = folds
        self.split = split

    @staticmethod
    def load_data(filename):
        """

        :param name: name of the CSV file to be loaded
        :return: loaded data as a pandas dataframe
        """
        try:
            df = pd.read_csv(filename)
            return df
        except Exception as e:
            print(e)
            print("Error Loading CSV file!")

    @staticmethod
    def normalize_data(df, cols):
        """

        :param df: dataframe to be normalized
        :param cols:  list of column names in the data
        :return: numpy format of the normalized data
        """
        try:
            x = df[cols[:-1]].values  # get all the columns data in a form of numpy array
            min_max_scaler = MinMaxScaler()
            x_scaled = min_max_scaler.fit_transform(x)
            df = pd.DataFrame(x_scaled, columns=cols[:-1])
            X = df.values
            return X
        except Exception as e:
            print(e)
            print("Error occurred in normalizing data")

    @staticmethod
    def encode_labels(target):

        try:
            le = LabelEncoder()
            le = le.fit(target)
            labels = le.transform(target)
            return labels
        except Exception as e:
            print(e)
            print("Error occurred while encoding labels")

    def train(self, x_train, y_train):

        try:
            param_grid = {
                'learning_rate': [0.0001, 0.001, 0.01, 0.1],
                'n_estimators': [100, 200, 300, 400, 500]
            }

            model = XGBClassifier()
            kfold = StratifiedKFold(n_splits=self.folds, shuffle=True, random_state=7)
            grid_search = GridSearchCV(model, param_grid, scoring="neg_log_loss", n_jobs=self.procs, cv=kfold,
                                       verbose=2)
            grid_result = grid_search.fit(x_train, y_train)
            return grid_result
        except Exception as e:
            print(e)
            print("Error occurred while XGBoost Training!")

    def main(self):

        df = self.load_data(self.filename)  # loading data from csv file
        df = df.drop("id", axis=1)  # dropping unwanted column named id

        # seperating out the target column from the data and getting the columns list
        cols = list(df.columns)  # list of column names
        print("Number of columns in the data: {}".format(str(len(cols))))
        target = df[cols[-1]]  # target column to be predicted
        print("No of classes in the data: {}".format(str(target.unique())))

        # normalize the data
        x = self.normalize_data(df, cols)

        # encoding target variables into numeric from categorical values
        labels = self.encode_labels(target)

        # take a subset of training data and labels of the ~61,000 samples
        inds = random.sample(range(1, x.shape[0]), 10000)
        x = x[inds, :]
        labels = labels[inds]

        # splitting data into training and testing
        x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=self.split, random_state=42)

        # train the XGBoost
        learning_rate = [0.0001, 0.001, 0.01, 0.1]
        n_estimators = [100, 200, 300, 400, 500]
        start = time.time()
        grid_result = self.train(x_train, y_train)
        stop = time.time()
        print("Time Elapsed for training: {} seconds".format(str(stop - start)))

        # print statistics
        try:
            print("Best Score: %f using best parameters: %s" % (grid_result.best_score_, grid_result.best_params_))
            means = grid_result.cv_results_['mean_test_score']
            stds = grid_result.cv_results_['std_test_score']
            params = grid_result.cv_results_['params']
            for mean, stdev, param in zip(means, stds, params):
                print("%f (%f) with: %r" % (mean, stdev, param))

            scores = np.array(means).reshape(len(learning_rate), len(n_estimators))
            for i, value in enumerate(learning_rate):
                plt.plot(n_estimators, scores[i], label='learning_rate: ' + str(value))
            plt.legend()
            plt.xlabel('n_estimators')
            plt.ylabel('Log Loss')
            plt.savefig("n_estimators_vs_learning_rate_" + str(procs) + ".png")
        except Exception as e:
            print(e)
            print("Error displaying run statistics and plotting graphs!")


if __name__ == "__main__":

    try:
        procs = int(input("Enter the number of processors to be used: "))
    except Exception as e:
        procs = 1
        print(e)
        print("number of processors cannot be more than 48!")

    p = Part3(filename="train.csv", procs=procs, folds=10, split=0.2)
    p.main()
