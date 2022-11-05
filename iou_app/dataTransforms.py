def getItemDetails(items, field_name):
    total_amount = 0
    details = {}
    for item in items:
        if(item[field_name] in details):
            details[item[field_name]] += item['amount']
        else:
            details[item[field_name]] = item['amount']
        total_amount += details[item[field_name]]
    return (total_amount, details)


def getUserObj(user_name, owes_items, lent_items):
    if(type(owes_items) != list and type(lent_items) != list):
        return {}
    total_owed, owes_items = getItemDetails(owes_items, 'lender')
    total_lent, lent_items = getItemDetails(lent_items, 'borrower')
    user_obj = {
        'name': user_name,
        'owes': owes_items,
        'owed_by': lent_items,
        'balance': f'<({total_lent})-({total_owed})>'
    }
    return user_obj
