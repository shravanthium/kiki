def __display__(packages,show_eta=False):
    for package in packages:
        if show_eta:
            print(package.id, package.discount(), package.total_cost(),package.estimated_delivery_time)
        else:
            print(package.id, package.discount(), package.total_cost())