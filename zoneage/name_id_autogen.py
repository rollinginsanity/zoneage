"""
Functions to automatically generate IDs and the such...
"""

def generate_id(prefix, starting_number=0, increment=1):
    """

    :param prefix: The prefix we want to give all generated IDs, like F for flow, or N for node.
    :param starting_number: The number we want to start counting from.
    :param increment: The increment. if we want to shim nodes in later we should leave some space.
    :return: Yields the next ID.
    """

    i = starting_number

    while True:

        id_val = prefix+str(i)

        i = i+increment

        yield id_val


zone_id_gen = generate_id("Z")
node_id_gen = generate_id("N", increment=2)
flow_id_gen = generate_id("F", increment=2)
