from binary_tree_priority_queue import Node, PriorityQueue

class Participant(Node):
    def __init__(self, participant_id, name, registration_time):
        self.id = participant_id
        self.name = name
        self.registration_time = registration_time
        super().__init__(value=self, priority=-participant_id)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Registered at: {self.registration_time}"

def quick_sort_participants(participants):
    if len(participants) <= 1:
        return participants
    pivot = participants[0]
    left = [p for p in participants[1:] if p.id < pivot.id]
    right = [p for p in participants[1:] if p.id >= pivot.id]
    return quick_sort_participants(left) + [pivot] + quick_sort_participants(right)

class RegistrationSystem:
    def __init__(self):
        self.queue = PriorityQueue()
        self.index = {}

    def register(self, participant_id, name, registration_time):
        if participant_id in self.index:
            print(f"Participant with ID {participant_id} already registered.")
            return
        participant = Participant(participant_id, name, registration_time)
        self.queue.root = self.queue._insert(self.queue.root, participant)
        self.index[participant_id] = participant
        print(f"Registered: {participant}")

    def remove_participant(self):
        if self.queue.root is None:
            print("No participants to remove.")
            return
        removed = self.queue.extract_max()
        if removed:
            participant = removed[0]
            del self.index[participant.id]
            print(f"Removed: {participant}")

    def find_by_id(self, participant_id):
        participant = self.index.get(participant_id)
        if participant:
            print(participant)
        else:
            print(f"Participant with ID {participant_id} not found.")

    def list_all_sorted(self):
        sorted_participants = quick_sort_participants(list(self.index.values()))
        for participant in sorted_participants:
            print(participant)

if __name__ == "__main__":
    reg = RegistrationSystem()

    reg.register(5, "Anna", "10:00")
    reg.register(2, "Bohdan", "10:05")
    reg.register(8, "Oksana", "10:10")

    print("\nПошук за ID 2:")
    reg.find_by_id(2)

    print("\nУсі учасники у порядку ID:")
    reg.list_all_sorted()

    print("\nВидалення учасника з найменшим ID:")
    reg.remove_participant()

    print("\nЗалишок учасників:")
    reg.list_all_sorted()
