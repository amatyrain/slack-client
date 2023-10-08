import slackweb


class SlackClient:
    def send_slack_message(self, url, message):
        slack = slackweb.Slack(url=url)
        slackbot_icon_emoji = ":ghost:"
        slackbot_username = 'webhookbot'

        slack.notify(
            text=message,
            icon_emoji=slackbot_icon_emoji,
            username=slackbot_username,
        )
