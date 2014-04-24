class RPSLS

  WHAT_BEATS_WHAT = { rock: {lizard: 'crushes', scissors: 'crushes'},
                                      paper: {rock: 'covers', spock: 'disproves'},
                                      scissors: {paper: 'cuts', lizard: 'decapitates'},
                                      lizard: {spock: 'poisons', paper: 'eats'},
                                      spock: {scissors: 'smashes', rock: 'vaporizes'}
                                    }

  def initialize
    @user_wins = 0
    @computer_wins = 0
    @tie_count = 0
  end

  def play
    user_input = get_and_clean_input
    if WHAT_BEATS_WHAT[user_input]
      computer_selection = get_computer_selection
      if user_input == computer_selection
        @tie_count += 1
        puts 'Tie!'
      else
        determine_winner(user_input, computer_selection)
      end
    else
      puts 'Invalid input!'
    end
  end

  private

  def get_and_clean_input
    puts "What's your choice? Rock, Paper, Scissors, Lizard, or Spock? Type 'quit' to quit."
    user_input = gets.chomp
    user_input == 'quit' ? finish_loop : (user_input = user_input.downcase.to_sym)
  end

  def get_computer_selection
    computer_selection = WHAT_BEATS_WHAT.keys.sample(1).first
    puts "Computer chooses #{ computer_selection.to_s.capitalize }"
    computer_selection
  end

  def determine_winner(user, computer)
    if WHAT_BEATS_WHAT[user][computer]
      puts "#{ user.to_s.capitalize } #{ WHAT_BEATS_WHAT[user][computer] } #{ computer.to_s.capitalize }" # e.g. rock crushes scissors
      puts "You win!\n-----"
      @user_wins += 1
    else
      puts "#{ computer.to_s.capitalize } #{ WHAT_BEATS_WHAT[computer][user] } #{ user.to_s.capitalize }"
      puts "Computer wins!\n-----"
      @computer_wins += 1
    end
  end

  def finish_loop
    abort "Games over.\n You won #{ @user_wins } times and the computer won #{ @computer_wins } times. There were #{ @tie_count } ties."
  end

end

game = RPSLS.new
game.play while true
