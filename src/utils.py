import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler


def get_tsne_plot(X, y, title='T-SNE', n_components=2, x_size=6, y_size=4):
    tsne = TSNE(n_components=n_components)
    X_embedded = tsne.fit_transform(X)
    plt.figure(figsize=(x_size, y_size))
    sc = plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y, cmap='viridis')
    plt.colorbar(sc)
    plt.title(title)
    plt.show()


def get_standarized_data(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled


def plot_loss_and_metric(history, metric='accuracy', val_present=True):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Train')
    if val_present:
        plt.plot(history.history['val_loss'], label='Validation')
    plt.title('Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history[metric], label='Train')
    if val_present:
        plt.plot(history.history[f'val_{metric}'], label='Validation')
    plt.title(metric)
    plt.legend()
    plt.show()
