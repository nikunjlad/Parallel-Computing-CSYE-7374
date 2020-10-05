import multiprocessing as mp
import time
import numpy as np
from sklearn import svm

def cvkfold(X, y, tuning_params, partitions, k):
    n_tuning_params = tuning_params.shape[0]

    partition = partitions[k]
    Train = np.delete(np.arange(0, X.shape[0]), partition)
    Test = partition
    X_train = X[Train, :]
    y_train = y[Train]

    X_test = X[Test, :]
    y_test = y[Test]

    accuracies = np.zeros(n_tuning_params)
    for i in range(0, n_tuning_params):
        svc = svm.SVC(C = tuning_params[i], kernel = "linear")
        accuracies[i] = svc.fit(X_train, y_train).score(X_test, y_test)
    return accuracies

def log_results(X, y, tuning_params, partitions, k, arr):
    Accuracies = cvkfold(X, y, tuning_params, partitions, k)
    arr.append(Accuracies)

def process_processing(time_dict):
    print("Running the Process Paralleize function. ")
    with mp.Manager() as manager:
        res_vals = manager.list()
        st = time.time()
        processes = []

        test = np.loadtxt("optdigits.txt", delimiter=",")
        X = test[:, 0:64]
        y = test[:, 64]

        K = 4
        tuning_params = np.logspace(-6, -1, 10)
        partitions = np.array_split(np.random.permutation([i for i in range(0, X.shape[0])]), 16)

        for k in range(0, 4):
            p = mp.Process(target=log_results, args=(X, y, tuning_params, partitions, 16, res_vals))
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
        results = res_vals
        time_taken = time.time() - st
        print(f'Process runs for {(time.time() - st)} seconds.')
        final_results = []
        for i in results:
            mean_accuracy = np.mean(i)
            final_results.append(mean_accuracy)

        max_acc_folds = np.argmax(final_results)
        max_acc = final_results[np.argmax(final_results)]
        # print('CV max accuracy %0.6f.' %  (max(CV_accuracy)))
        print(f'The max CV accuracy was for {max_acc_folds + 1} folds and the accuracy was {max_acc}')
        best_tuning_param = tuning_params[np.argmax(results[max_acc_folds])]
        print('Best tuning param %0.6f.' % best_tuning_param)
    time_dict["Process"] = time_taken
    print("###########################################################################################################")
    return time_dict

time_dict = {}
print(process_processing(time_dict))