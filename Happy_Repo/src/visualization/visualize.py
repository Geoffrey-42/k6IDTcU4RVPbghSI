fig, ax = plt.subplots(2, 3, figsize = (16,8))
m, n = X_train.shape

neg = y_train == 0
pos = y_train == 1


for k in range(6):
    x_neg, y_neg = np.array(X_train[['X%s'%1]][neg], dtype = 'float64').reshape(-1), np.array(X_train[['X%s'%(k+1)]][neg], dtype = 'float64').reshape(-1)
    x_pos, y_pos = np.array(X_train[['X%s'%1]][pos], dtype = 'float64').reshape(-1), np.array(X_train[['X%s'%(k+1)]][pos], dtype = 'float64').reshape(-1)

    move = 0.25
    x_neg += np.random.uniform(-move,move, size = len(x_neg))
    y_neg += np.random.uniform(-move,move, size = len(x_neg))

    x_pos += np.random.uniform(-move,move, size = len(x_pos))
    y_pos += np.random.uniform(-move,move, size = len(x_pos))
    i, j = k//3, k%3
    ax[i][j].scatter(x_neg, y_neg, marker = 'x', c = 'red', s = 20, label = 'y = 0')
    ax[i][j].scatter(x_pos, y_pos , marker = 'o', c = 'blue', s = 25, label = 'y = 1')
    ax[i][j].set_ylabel('$X_%s$'%(k+1), fontsize = 12)
    ax[i][j].set_xlabel('$X_1$', fontsize = 12)
    ax[i][j].set_title('Plot for variables X1 and X%s with small (<%s) random variations of the note'%(k+1, move), fontsize = 8)
    ax[i][j].legend()
    plt.tight_layout()

plt.show()
