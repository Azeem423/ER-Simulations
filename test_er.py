import unittest
from hw10 import Patient, PriorityQueue, EmergencyRoom


'''class to test the functionality of the EmergencyRoom, Patient, and PriorityQueue classes.'''
class TestEmergencyRoom(unittest.TestCase):
    def setUp(self):
        self.er = EmergencyRoom()



    def test_no_patients(self):
        """Test that the emergency room handles having no patients."""
        with self.assertRaises(IndexError):
            self.er.treat_patient()



    '''Test the creation of a Patient object'''
    def test_patient(self):
        patient1 = Patient("Azeem", 5)  # giving patient name
        patient2 = Patient("Zing", 7)   # giving patient name

        self.assertEqual(patient1.name, "Azeem")
        self.assertEqual(patient1.severity, 5)
        self.assertTrue(patient1 > patient2)


    
    '''Test the push and pop operations in the priority queue.'''
    def test_priority_queue(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())

        #names for the patients
        patient1 = Patient("Yous", 1)
        patient2 = Patient("Eman", 6)

        pq.push(patient1)
        self.assertFalse(pq.is_empty())
        pq.push(patient2)
        self.assertEqual(pq.pop().name, "Eman")



    
    '''Test the overall simulation process in the EmergencyRoom class.
        Ensure that your unittests cover various scenarios, including edge cases.'''

    def test_emergency_room(self):
        # Provide a name for the patient
        patient = Patient("Sabr", 5)

        self.er.admit_patient(patient)
        self.er.treat_patient()
        self.assertEqual(self.er.treated_patients[0].name, "Sabr")

if __name__ == "__main__":
    unittest.main()
