import random

class Revolver():
    def __init__(self):
        self.revolver_drum = ['No bullet']*6
        self.curent_slot_position = 0

    def add_bullet(self,bullet):
        for slot in self.revolver_drum:
            if slot == 'No bullet':
                self.revolver_drum[self.revolver_drum.index(slot)] = bullet
                return True
        else:
            return False

    def add_bullet_from_list(self,list):
        if self.revolver_drum.count('No bullet') == 0 or len(list) == 0:
            return False
        else:
            for bullet_from_list in list:
                for slot_in_revolver in self.revolver_drum:
                    if slot_in_revolver == 'No bullet':
                        self.revolver_drum[self.revolver_drum.index(slot_in_revolver)] = bullet_from_list
                        break
            return True

    def shoot(self):
        if self.revolver_drum[self.curent_slot_position%6] != 'No bullet':
            self.revolver_drum[self.curent_slot_position % 6] = 'No bullet'
            self.curent_slot_position += 1
            return 'Successful shot'
        else:
            return None

    def unload(self,all_items = False):
        if all_items == False:
            if self.revolver_drum[self.curent_slot_position%6] != 'No bullet':
                self.revolver_drum[self.curent_slot_position % 6] = 'No bullet'
                return self.revolver_drum[self.curent_slot_position%6]
            else:
                return None

        else:
            for_return_revolver_drum = self.revolver_drum.copy()
            self.revolver_drum = ['No bullet']*6
            return for_return_revolver_drum

    def scroll(self):
        self.curent_slot_position = random.randint(0,5)

    def bullet_count(self):
        return 6 - self.revolver_drum.count('No bullet')

    ## other

    def view_revolver_drum(self):
        print(self.revolver_drum)

    def view_current_slot_position(self):
        print(self.curent_slot_position%6)


revolver = Revolver()

# add bullet
print(revolver.add_bullet('bullet') , 'adding bullet')
print(revolver.add_bullet_from_list(['bullet from list 1', 'bullet from list 2']) ,'adding bullet from list')
revolver.view_revolver_drum()

print('-'*100)

#shooting
print(revolver.shoot())
revolver.view_revolver_drum()
revolver.view_current_slot_position()

print('-'*100)

#unloading
print(revolver.unload() , ' ||| unloading in current slot position')
revolver.view_revolver_drum()
print(revolver.unload(all_items=True),'||| unloading all revolver drum')
revolver.view_revolver_drum()

#scrolling

print('-'*100)
revolver.view_current_slot_position()
revolver.scroll()
revolver.view_current_slot_position()

#bullet_count
print('-'*100)
print(revolver.bullet_count())