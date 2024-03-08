Lottery Scheduler
This is a lottery scheduler written in Python. The lottery scheduler is by far one of the hardest
scheduling algorithms i think I have ever come across. It is used in computer systems to randomly
select processes for execution based on the number of lottery tickes assigned to each process.

How it works
The program is broken up into 2 classes
The first one is Process, represents a process in the lottery scheduler. It uses ProcessId and LotteryTickets
using these identifiers and tickets, it is able to help distinguish it from other processes in the system
and to determine the likelihood of selecting a process for execution.

