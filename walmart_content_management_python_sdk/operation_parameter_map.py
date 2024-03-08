operation_parameter_map = {
    '/v3/feeds-POST': {
        'parameters': [
            {
                'name': 'feedType'
            },
            {
                'name': 'WM_QOS.CORRELATION_ID'
            },
            {
                'name': 'WM_SVC.NAME'
            },
            {
                'name': 'WM_SEC.TIMESTAMP'
            },
            {
                'name': 'WM_SEC.AUTH_SIGNATURE'
            },
            {
                'name': 'WM_CONSUMER.ID'
            },
            {
                'name': 'file'
            },
            {
                'name': 'WM_CONSUMER.CHANNEL.TYPE'
            },
        ]
    },
    '/v2/feeds-POST': {
        'parameters': [
            {
                'name': 'feedType'
            },
            {
                'name': 'WM_QOS.CORRELATION_ID'
            },
            {
                'name': 'WM_SVC.NAME'
            },
            {
                'name': 'WM_SEC.TIMESTAMP'
            },
            {
                'name': 'WM_SEC.AUTH_SIGNATURE'
            },
            {
                'name': 'WM_CONSUMER.ID'
            },
            {
                'name': 'WM_CONSUMER.CHANNEL.TYPE'
            },
        ]
    },
    '/feeds-GET': {
        'parameters': [
            {
                'name': 'feedId'
            },
            {
                'name': 'WM_QOS.CORRELATION_ID'
            },
            {
                'name': 'WM_SVC.NAME'
            },
            {
                'name': 'WM_SEC.TIMESTAMP'
            },
            {
                'name': 'WM_SEC.AUTH_SIGNATURE'
            },
            {
                'name': 'WM_CONSUMER.ID'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'WM_CONSUMER.CHANNEL.TYPE'
            },
        ]
    },
    '/feeds/{feedId}-GET': {
        'parameters': [
            {
                'name': 'feedId'
            },
            {
                'name': 'WM_QOS.CORRELATION_ID'
            },
            {
                'name': 'WM_SVC.NAME'
            },
            {
                'name': 'WM_SEC.TIMESTAMP'
            },
            {
                'name': 'WM_SEC.AUTH_SIGNATURE'
            },
            {
                'name': 'WM_CONSUMER.ID'
            },
            {
                'name': 'includeDetails'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'WM_CONSUMER.CHANNEL.TYPE'
            },
        ]
    },
};