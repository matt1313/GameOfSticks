Actors:
User
AI

Major Game Components:
class GamePlay
class AI
class UserInteraction
class OutOfRangeError
main() function

class OutOfRangeError(Exception):
exception for if users input is out of range.
   pass

class GamePlay:
   def init:
       get_players(self, player_one= 0, player_two= 0, starting_sticks) >> class UserInteraction -- P vs P or P vs AI
           if UserInteraction.get_players() == 2:
               self.player_one = player_one
               self.player_two = player_two
           elif UserInteraction.get_players() == 1
               self.player_one = player_one
               self.player_two = player_ai
           self.starting_sticks = UserInteraction.get_starting_num_sticks()



game play
   def main():
       game1 = GamePlay()
       ui = UserInteraction()
       do we need two UserInteraction objects, one for each player?
       whose_turn = 0
       turn_count = 1
       stick_count = game1.starting_sticks

       while stick_count > 1:
           if stick_count == 1 and whose_turn == player:
               player looses
           else:
               if turn_count % 2 != 0
                   whose_turn = player_one
               else:
                   whose_turn = player_two
           print(whose_turn) -- is it better to have a display function?
           player_one_pick_up_count = UserInteraction.take_turn()  >> class UserInteraction or class AI
           if player_two != player_ai:
               player_one_pick_up_count = UserInteraction.take_turn()  >> class UserInteraction or class AI
           else:
               player_two_pick_up_count = UserInteraction.take_turn()
           stick_count - (player_one_pick_up_count + player_two_pick_up_count)
           display sticks remaining


class player:

    def take_turn():
        acceptable_inputs = [1, 2, 3]
        try:
            pick_up_num = int(input("How many sticks would you like to pick up? 1, 2, 3: "))
        except:
            if pick_up_num not in acceptable_inputs:
                raise OutOfRangeError()
        return pick_up_num

        needs to account for remaining sticks

class UserInteraction:

   def get_players():
       number_players = input("Enter number of players: ")
       return number_players

   def get_starting_num_sticks():
       starting_num_sticks = int(input('Enter how sticks you would like to with: '))
       if user_input < 10 or user_input 100 >:
           raise OutOfRangeError()

       else:
           return starting_num_sticks



   main()
class AI:
   outer_list = [creates number of inner list objects based on number of sticks remaining] >> class UserInteraction -- get_starting_stick_count
   uses number of sticks remaining as index position for choice list -- how do we account for the inner list at position [0]?
   inner_list = [1,2,3]
   ai_choice = random.choice(outer_list[stick_count])
   if the ai's choice at given index led to it winning:
       inner_list.insert(given index) -- insert number of sticks picked up ie 1, 2, or 3
       inner_list[3] = [1,2,3,2]
   if the ai's choice led to it losing:
       remove ai's choice from position
           inner_list[3] = [2,3]
