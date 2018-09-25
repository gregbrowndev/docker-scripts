from airflow.operators.slack_operator import SlackAPIOperator


class SlackAPIFileUploadOperator(SlackAPIOperator):

    def __init__(self,
                 channels='#general',
                 username='Airflow',
                 title=None,
                 file=None,
                 *args, **kwargs):
        self.method = 'files.upload'
        self.channels = channels
        self.username = username
        self.title = title
        self.file = file
        super(SlackAPIFileUploadOperator, self).__init__(method=self.method,
                                                         *args, **kwargs)

    def construct_api_call_params(self):
        self.api_params = {
            'channels': self.channels,
            'username': self.username,
            'title': self.title(),
            'file': self.file()
        }
