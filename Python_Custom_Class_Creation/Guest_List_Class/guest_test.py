from task_guest import Guest

Guest1 = Guest("Andrew Simmons","Chicago","Mentor")
Guest2 = Guest("Dannie Smith","Atlanta","Manager")
Guest3 = Guest("Celine Dion","Montreal","Singer")

guest_list = [Guest1, Guest2, Guest3]

for guest in guest_list:
    print(guest.guest_info())
