
# What a “job” is in this system?

It is a task that the client wants to be performed in order to get a desired result, which would be executed asynchronously due to the time-consuming nature of the task. It has persistent data: it has a payload that stores needed data to run the task, has date data associated with the job, and metadata to know performance and categorize the jobs. At the end the state would end as completed when it gives an output result, or dead when failed multiple times, defined by a retry limit, and could fail also when it lasts longer than a timeout.

# What does “asynchronous processing” mean?

Asynchronous processing is the opposite of synchronous processing: after making a request, the client does not have to wait for a response and can continue with other processing tasks. This process is referred to as 'non-blocking' because the client's execution thread is not blocked after the request is made. This allows systems to potentially scale more effectively, as more work can be completed within a given timeframe.

# Important metadata to store

- Execution time.
- Retries count.
- Error messages (if failed).
- Creation, start and completion or dead date time.
- Job type.
- Payload.
- Result.
- Status.

# Retry policy

Retry limit: 3 retries.
The retry will be executed immediately after a timeout exception occurs.

Timeout time: 30 seconds.
Future versions may implement adaptive retry strategies.

# What makes a job “failed”?

A job is considered failed, if the time that takes to complete the task exceeds the timeout time, or if an error occurs when trying to process the desired result. However, a job is not considered “failed” if the system crashes, or the thread is interrupted before finishing, but the performing task could be inconsistent, therefore, when the system starts up, it will check the running process, and start a thread for a new, clean performance without considering the inconsistent previous performance. 

If a process keeps on pending and never start running, there will be a periodic recovery mechanism that detects pending jobs that were created X time ago, to prevent errors with the ones created recently, and transition them to running state cause failed state should be reached from running state.