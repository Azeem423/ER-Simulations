import random

class Patient:
    def __init__(self, name, severity):
        """
        Initialize a Patient object.
        Parameters:
        - name (str): The name of the patient.
        - severity (int): The severity level of the patient's condition.
        """
        self.name = name
        self.severity = severity

    def __lt__(self, other):
        """
        Compare two patients based on severity for priority queue ordering.
        Parameters:
        - other (Patient): Another patient to compare.
        Returns:
        - bool: True if the current patient has higher priority (lower severity), False otherwise.
        """
        return self.severity > other.severity

class PriorityQueue:
    def __init__(self):
        """Initialize an empty priority queue."""
        self._entries = []

    def is_empty(self):
        """
        Check if the priority queue is empty.
        Returns:
        - bool: True if the priority queue is empty, False otherwise.
        """
        return len(self._entries) == 0

    def push(self, item):
        """
        Add an item to the priority queue.
        Parameters:
        - item: The item to add to the priority queue.
        """
        self._entries.append(item)
        self._upheap(len(self._entries) - 1)

    def pop(self):
        """
        Remove and return the item with the highest priority from the priority queue.
        Returns:
        - item: The item with the highest priority.
        """
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        self._swap(0, -1)
        item = self._entries.pop()
        self._downheap(0)
        return item

    def _parent(self, i):
        """
        Get the index of the parent of the element at index i.
        """
        return (i - 1) // 2

    def _children(self, i):
        """
        Get the indices of the children of the element at index i.
        """
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))

    def _swap(self, a, b):
        """
        Swap elements at indices a and b in the priority queue.
        """
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        """
        Restore the heap order after adding an element to the end.
        """
        while i > 0 and self._entries[i] < self._entries[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _downheap(self, i):
        """
        Restore the heap order after removing the root element.
        """
        while True:
            min_index = i
            for j in self._children(i):
                if self._entries[j] < self._entries[min_index]:
                    min_index = j
            if min_index == i:
                return
            self._swap(i, min_index)
            i = min_index

class EmergencyRoom:
    def __init__(self):
        """Initialize an EmergencyRoom object with an empty waiting room."""
        self.waiting_room = PriorityQueue()
        self.treated_patients = []

    def admit_patient(self, patient):
        """
        Admit a patient to the emergency room.
        Parameters:
        - patient (Patient): The patient to admit.
        """
        self.waiting_room.push(patient)
        print(f"{patient.name} admitted to the emergency room with severity {patient.severity}.")

    def treat_patient(self):
        """Treat the next patient in the waiting room, if any."""
        if self.waiting_room.is_empty():
            raise IndexError()

        else:
            patient = self.waiting_room.pop()
            self.treated_patients.append(patient)
            print(f"Treated {patient.name} with severity {patient.severity}.")

    def simulate_emergency_room(self, num_patients):
        """
        Simulate the operation of the emergency room.
        """
        for i in range(num_patients):
            name = f"Patient-{i+1}"
            severity = random.randint(1, 10)  # Severity level is randomly assigned
            patient = Patient(name, severity)
            self.admit_patient(patient)

        while not self.waiting_room.is_empty():
            self.treat_patient()

if __name__ == "__main__":
    er = EmergencyRoom()
    er.simulate_emergency_room(10)
