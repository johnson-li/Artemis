def get_instance_name(instance):
    if not instance or not instance.tags:
        return 'None'
    for pair in instance.tags:
        if pair['Key'] == 'Name':
            return pair['Value']
    return 'None'
