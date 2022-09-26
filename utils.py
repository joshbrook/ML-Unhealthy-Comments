import os
import matplotlib.pyplot as plt


def save_fig(
    fig_id,
    tight_layout=True,
    fig_extension="png",
    resolution=300,
    img_path="",
):
    """Simple function to save the most recently created figure in a
    standardised way

    :param fig_id: Name for the saved figure file
    :param tight_layout: Boolean denoted whether to use a tight layout
    (see matplotlib documentation)
    :param fig_extension: file type to be used for the figure
    :param resolution: image resolution of the saved image
    :param img_path: path to store image. Default is current folder
    :returns: None
    :rtype: None

    """
    path = os.path.join(img_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    

def true_false_plot(
    y_true,
    y_pred,
    fig_id,
    tight_layout=True,
    fig_extension="png",
    resolution=300,
    img_path="",
):
    """Function to draw true vs false predictions scatter plot and save to file

    :param y_true: array of true values
    :param y_pred: array of predicted values
    :param fig_id: name of saved figure
    :param tight_layout: Boolean denoted whether to use a tight layout
    (see matplotlib documentation)
    :param fig_extension: file type to be used for the figure
    :param resolution: image resolution of the saved image
    :param img_path: path to store image. Default is current folder
    :returns: Name of stored figure
    :rtype: string

    """
    plt.scatter(y_true, y_pred)
    xpoints = ypoints = plt.xlim()
    plt.plot(
        xpoints,
        ypoints,
        linestyle="--",
        color="k",
        lw=3,
        scalex=False,
        scaley=False,
    )
    plt.xlabel("True Value")
    plt.ylabel("Predicted Value")
    plt.title("True vs Predicted Value")
    save_fig(fig_id, resolution=resolution, img_path=img_path)
    path = os.path.join(img_path, fig_id + "." + fig_extension)
    return ("stored plot to in:", path)
