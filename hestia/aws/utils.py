def get_instance_name(instance):
    for pair in instance.tags:
        if pair['Key'] == 'Name':
            return pair['Value']
    return 'None'
