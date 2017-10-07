from django.db import models

class User(models.Model):
    firstName = models.TextField(max_length=255)
    lastName = models.TextField(max_length=255)
    rewardCount = models.IntegerField(default=0)
    rewardProgress = models.IntegerField(default=0)
    surveyCount = models.IntegerField(default=0)

    def getRewardProgress(self):
        return self.rewardCount

    def giveReward(self):
        self.rewardProgress = 0
        self.rewardCount = self.rewardCount+1