"""Main module."""

import graphviz


class DrawNN:
    """ """

    def __init__(self, layers, nn_type='ANN'):
        self.layers = layers

        # init neural network
        nn = graphviz.Graph()
        nn.label = "layer 1 (input layer)"
        for layer_num, n_nodes in enumerate(layers):
            if layer_num + 1 < len(layers):
                next_n_nodes = layers[layer_num + 1]
                for node in range(n_nodes):
                    if nn_type is 'RNN' and layer_num is not 0:
                        nn.edge('L' + str(layer_num) + '-' + str(node + 1),
                                'L' + str(layer_num) + '-' + str(node + 1))
                    for next_node in range(next_n_nodes):
                        nn.edge('L' + str(layer_num) + '-' + str(node + 1),
                                'L' + str(layer_num + 1) + '-' + str(next_node + 1))

        self.graph_object = nn

    def draw(self,
             direction='LR',
             linewidth=1,
             size='4,4!',
             fillcolor=None,
             node_labels=None,
             graph_label=None,
             node_fontsize=10,
             graph_fontsize=12,
             node_fontcolor='#000000',
             graph_fontcolor='#000000',
             fontname='helvetica'):
        """

        Parameters
        ----------
        direction : str
             (Default value = 'LR')
        linewidth : float
             (Default value = 1)
        size : str
             (Default value = '4,4!')
        fillcolor : str
             (Default value = None)
        node_labels : bool or str
             (Default value = None)
        graph_label : str
             (Default value = None)
        node_fontsize : float
             (Default value = 10)
        graph_fontsize : float
             (Default value = 12)
        node_fontcolor : str
             (Default value = '#000000')
        graph_fontcolor : str
             (Default value = '#000000')
        fontname : str
             (Default value = 'helvetica')

        Returns
        -------

        """

        self.graph_object.attr(rankdir=direction, size=size)

        # fonts
        self.graph_object.node_attr["fontsize"] = "{}".format(node_fontsize)
        self.graph_object.graph_attr["fontsize"] = "{}".format(graph_fontsize)
        self.graph_object.node_attr["fontname"] = fontname
        self.graph_object.graph_attr["fontname"] = fontname
        self.graph_object.node_attr["fontcolor"] = node_fontcolor
        self.graph_object.graph_attr["fontcolor"] = graph_fontcolor

        self.graph_object.node_attr["fixedsize"] = "false"
        self.graph_object.edge_attr["style"] = "setlinewidth({})".format(linewidth)
        self.graph_object.node_attr["style"] = "filled"
        if fillcolor is not None:
            self.graph_object.node_attr["fillcolor"] = fillcolor
        else:
            self.graph_object.node_attr["fillcolor"] = "#D3D3D3"
        self.graph_object.node_attr["shape"] = "circle"
        self.graph_object.node_attr["fixedsize"] = "true"
        if node_labels is None:
            self.graph_object.node_attr["label"] = ""
        elif node_labels is True:
            pass
        else:
            self.graph_object.node_attr["label"] = node_labels
        if graph_label is not None:
            self.graph_object.graph_attr["label"] = graph_label
        return self.graph_object

    def save(self,
             filename='nntecture',
             output_format='pdf',
             size='4,4!',
             directory=None,
             cleanup=True,
             view=True):
        """

        Parameters
        ----------
        filename :
             (Default value = 'nntecture')
        output_format :
             (Default value = 'pdf')
        size :
             (Default value = '4)
        4!' :

        directory :
             (Default value = None)
        cleanup :
             (Default value = True)
        view :
             (Default value = True)

        Returns
        -------

        """
        self.graph_object.attr(size=size)
        self.graph_object.render(filename=filename,
                                 format=output_format,
                                 directory=directory,
                                 cleanup=cleanup,
                                 view=view)
