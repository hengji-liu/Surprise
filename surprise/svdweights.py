from collections import Counter


def complement_appearance(trainset):
    """
    given a trainset, construct weights for every product
    trainset is 0..nbr_max
    weights in the same order
    :param trainset:
    :return:
    """
    item_presence = [i for (u, i, r) in trainset.all_ratings()]
    cnt = Counter(item_presence)
    presence_order_by_inner_id = [cnt[key] for key in sorted(cnt.keys())]
    max_presence = max(presence_order_by_inner_id)
    return [(max_presence - val + 1) for val in presence_order_by_inner_id]


def appearance(trainset):
    """
    given a trainset, construct weights for every product
    trainset is 0..nbr_max
    weights in the same order
    :param trainset:
    :return:
    """
    item_presence = [i for (u, i, r) in trainset.all_ratings()]
    cnt = Counter(item_presence)
    presence_order_by_inner_id = [cnt[key] for key in sorted(cnt.keys())]
    return presence_order_by_inner_id

    # appearance are from 1..97
    # complement_appearance 97..1
    # log complement_appearance (softened if compare to vanilla appearance)

    # maybe give more emphasis on the middle range products? construct a function like this -> /--\ sin?
    # consider the steepness of the slope
