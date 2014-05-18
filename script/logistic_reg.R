setwd("~/kaggle/kdd_2014/")
library("data.table")
dat = data.table(read.csv("data/intermediate/train_labeled.csv"))
dat$is_exciting_tf = (dat$is_exciting == 't')

fit <- glm(is_exciting_tf ~ log(students_reached), family=binomial, data=dat)
summary(fit)

submit_dat = data.table(read.csv("data/intermediate/submit.csv"))
submission = data.table(projectid=submit_dat$projectid, is_exciting = predict(fit, submit_dat, type="response"))
write.csv(submission, file ="data/submission/log_reg_1.csv", row.names=FALSE)

dat$pred = predict(fit, dat, type="response")