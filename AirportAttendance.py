import random
import decimal
global TicketID, PassengerID, PassengerSpot, PassengerServed

PassengerID = 1 #Value of passenger ID made global to be used in other methods, specifically for the queue when assigning PassengerID's and handleBeginService 
PassengerSpot = 0 #Distinct from ID as it is used to call specific passengers in the passenger list to use their respective methods 
PassengerServed = 0#Distinct from spot but serves same purpose of calling passengers from the list in handleEndService method
class Queue: #Basic queue class used for our passenger line
	def __init__(self, size = 1000):
		self.arr = []
		self.max = size


	def enqueue(self, d):
		if len(self.arr) >= self.max:
			print("Array full")
		else:
			self.arr.insert(0, d)


	def dequeue(self):
		if self.arr == []:
			return None
		else:
			return self.arr.pop()


	def isFull(self):
		if len(self.arr) >= self.max:
			return True
		else:
			return False

	def isEmpty(self):
		return self.arr == []

	def __str__(self):
		return str(self.arr)

	def size(self):
		return len(self.arr)


class Passenger:

	def __init__(self, idNum, arrivalTime):	#Creates a passenger object with their idNum and arrival time
		self._idNum = idNum
		self._arrivalTime = arrivalTime


	def idNum(self):
		return self._idNum	#Gets the passenger's id number

	def timeArrived(self):
		return self._arrivalTime #Gets the passenger's arrival time

	def waitTime(self, curTime): #The ideal in the program was to take the wait time of each individual passenger and calculate the average out of all of them.
		return curTime - self._arrivalTime

class TicketAgent:

	def __init__(self, idNum):	#Creates a ticket agent with their respective methods which are the most important factor in this whole simulation 
		self._idNum = idNum
		self._passenger = None
		self._stopTime = -1

	def idNum(self):
		return self._idNum	#Gets the ticket agent's id number

	def startService(self, passenger, stopTime): #Indicates the ticket agent has begun assisting a passenger
		self._stopTime = stopTime
		self._passenger = passenger
		
	def isAvailable(self): #Checks if the agent is attending a passenger or not
		if self._passenger == None:
			return True
		else:
			return False

	def checkStopTime(self): #Checks if the agent is attending a passenger or not
		if self._stopTime == -1 and self._passenger is not None:
			return True
		else:
			return False

	def isFinished(self): #Checks if ticket agent has finished attending the passenger
		self._passenger = None

	def clocktick(self): #Used to decrement the service time of an agent if they are attending a passenger and once it reaches below -1 it'll specify that there is no passenger
		self._stopTime = self._stopTime - 1
		if self._stopTime <= -2:
			self._passenger = None
			self._stopTime = -1


class TickerCounterSimulation:
	#Create a simulation obPassengerSpotect
	def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
 
		self._arriveProb = 1.0/betweenTime #between time represents time it takes for passenger to arrive in line
		self._serviceTime  = serviceTime #Time it takes to serve a passenger
		self._numMinutes = numMinutes #The number of minutes in our simulation
		self._numAgents = numAgents #The number of agents that will be in service

	#Simulation components
		self._passengerQ = Queue()#Represents line for passengers to keep track of how many are in line
		self._theAgents = [] #Represents our agents
		self._passengers = [] #Represents our passengers and as opposed to queue we can use the methods in this one
		for i in range(numAgents): 
			self._theAgents.append(TicketAgent(i+1)) #Assigns the TicketAgent class to each agent specified to inherit methods

	#Computed during the simulation
		self._totalWaitTime = 0 #Adds up the total wait time of passengers
		self._numPassengers = 0 #Specifies  num of passengers arrived

	#Run the simulation using the parameters supplied earlier

	def run(self):
		for curTime in range(1, self._numMinutes + 1): #Begins simulation and repeats every minute 
			self._handleArrive(curTime)
			self._handleBeginService(curTime)
			self._handleEndService(curTime)

	def printResults(self):
		numServed = self._numPassengers - self._passengerQ.size() #Calculates the number of people served
		avgWait = float(((self._totalWaitTime)) / numServed) #Gets average wait time by comparing the total number of passenger wait times
		print("")
		print("Number of passengers served = ", numServed) #Prints result of previous calculation for number of people served
		print("Number of passengers remaining in line = %d" %self._passengerQ.size()) #Specifies number of people still left in life
		print("The average wait time was %4.2f minutes." %avgWait) #

	def _handleArrive(self, curTime):
		num = decimal.Decimal(str(random.random()))#Generates random decimal to be compared below with arrival probability  
		global PassengerID#Will hold PassengerID for use it print
		if num <= self._arriveProb: #Checks if the generated number meets the requirement, if so a passenger has arrived, if not the program goes to handleBeginService
			newPassenger = Passenger(PassengerID, curTime) #Creates a newPassenger so that we can use the methods in the object for other functions in the program
			self._passengerQ.enqueue(newPassenger)#Adds passenger to line
			self._passengers.append(newPassenger)#Alternate line which is used to call methods of passengers in other parts of the program
			PassengerID += 1 #Increments to ID variable for to assign new one to next passenger
			print("Time Tick:", (curTime)) #Helps keep track of time ticks in our simulation
			print("Passenger arrived, ID:", newPassenger.idNum())#Specifies the passenger which arrived starting at 1
			self._numPassengers += 1 #Specifies the total number of passengers arrived has increased by 1

	def _handleBeginService(self, curTime):
			global PassengerSpot #Holds the spot of passengers with their respective ID to be used in the print statement
			for i in range (self._numAgents):#Begins loop to check all agents with the following if statement
				if (self._theAgents[i].isAvailable()) and (not self._passengerQ.isEmpty()): #If the agent is free then this statement will be true
					if PassengerSpot >= self._passengerQ.size():
						pass
					else:
						self._theAgents[i].startService(self._passengers[PassengerSpot], self._serviceTime) #Begins serving passenger for amounted service time
						print("Ticket Agent #", self._theAgents[i].idNum())
						print("Started Serving Passenger #", self._passengers[PassengerSpot].idNum())#Calls method of idNum for specific passenger in list depending on iteration
						PassengerSpot += 1 #assures that in the next iteration we will get the ID for the next passenger in line 
			for r in range (self._numAgents): #Loop to decrement service time so the agents will eventually become available
				self._theAgents[r].clocktick() #Decrements servicetime to agent which represents time passed serving the passenger until it reaches 0

	def _handleEndService(self, curTime): 
			global PassengerServed #Holds ID for specific passenger that was served
			for i in range (self._numAgents): #Begins loop to check all agents with the following if statement
				if (self._theAgents[i].checkStopTime()): #Checks to see if agent finished with passenger
					self._theAgents[i].isFinished() #Indicates that agent is now free to serve another passenger
					self._passengerQ.dequeue() #Calls queue to specify that passenger left line
					self._totalWaitTime += self._serviceTime
					print("(End)TicketAgent#", self._theAgents[i].idNum()) 
					print("Stopped Serving Passenger #", self._passengers[PassengerServed].idNum())
					PassengerServed += 1
			
c = TickerCounterSimulation(2,15,2,3) #Initializes our simulation with the variables
c.run() #runs methods depending on given minutes
c.printResults() #Prints results of simulation