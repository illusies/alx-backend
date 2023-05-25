/* A script that creates an array that will contain the blacklisted phone
 * numbers, a function (sendNotification) that tracks the progress of the job
 * of 0 out of 100, and a queue with Kue that will proceed the job of the 
 * queue push_notification_code_2 with two jobs at a time
 */

import kue from 'kue';

const blacklistedNum = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.track(0, 100);

  if (blacklistedNum.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.track(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
  done();
}

const queue = kue.createQueue();
const queueName = 'push_notification_code_2';

queue.process(queueName, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
