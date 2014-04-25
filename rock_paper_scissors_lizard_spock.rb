class RPSLS

  WHAT_BEATS_WHAT = { rock: {lizard: 'crushes', scissors: 'crushes'},
                      paper: {rock: 'covers', spock: 'disproves'},
                      scissors: {paper: 'cuts', lizard: 'decapitates'},
                      lizard: {spock: 'poisons', paper: 'eats'},
                      spock: {scissors: 'smashes', rock: 'vaporizes'}
                    }

  def initialize(smart)
    @user_wins = 0
    @computer_wins = 0
    @tie_count = 0
    @smart = smart
  end

  def play
    initialize_ai_memory if @smart
    user_input = get_and_clean_input
    if WHAT_BEATS_WHAT[user_input]
      computer_selection = get_computer_selection
      if user_input == computer_selection
        @tie_count += 1
        puts 'Tie!'
      else
        determine_winner(user_input, computer_selection)
      end
      save_user_input(user_input) if @smart
    else
      puts 'Invalid input!'
    end
  end

  private

  def initialize_ai_memory
    @USER_PICK_MEMORY ||= Hash[WHAT_BEATS_WHAT.keys.map { |k| [k, 0] }]
    @TOP_PICKS ||= []
  end

  def get_and_clean_input
    puts "What's your choice? Rock, Paper, Scissors, Lizard, or Spock? Type 'quit' to quit."
    user_input = gets.chomp
    user_input == 'quit' ? print_stats : (user_input = user_input.downcase.to_sym)
  end

  def get_computer_selection
    computer_selection = @smart ? smart_computer_selection : random_computer_selection
    puts "Computer chooses #{ computer_selection.to_s.capitalize }"
    computer_selection
  end

  def smart_computer_selection
    # Only start the guesswork after we collect some data
    if @USER_PICK_MEMORY.values.inject(0, :+) > 3
      most_picked = @USER_PICK_MEMORY.select{ |k,v| v == @USER_PICK_MEMORY.values.max }.keys
      @TOP_PICKS = store_top_pick(most_picked)
      counters = get_counter_moves(most_picked)
      counters.empty? ? random_computer_selection : counters.sample(1).first
    else
      random_computer_selection
    end
  end

  def random_computer_selection
    WHAT_BEATS_WHAT.keys.sample(1).first
  end

  def save_user_input(user_input)
    @USER_PICK_MEMORY[user_input] += 1
  end

  def store_top_pick(pick)
    @TOP_PICKS += pick
    @TOP_PICKS.uniq
  end

  def get_counter_moves(pick)
    counters = []
    pick.each { |p| counters += WHAT_BEATS_WHAT.select { |k,v| v[p] != nil }.keys }
    counters - @TOP_PICKS
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

  def print_stats
    puts "Games finished."
    puts "Player victories: #{ @user_wins }"
    puts "Computer victories: #{ @computer_wins }"
    puts "Ties: #{ @tie_count }"
    abort "You won #{ 100*(@user_wins.to_f / (@user_wins + @computer_wins + @tie_count).to_f).round(3) }% of #{ @user_wins + @computer_wins + @tie_count } games"
  end

end

puts "Do you want to play with the smarter AI? y/n"
smart = gets.chomp == 'y'
game = RPSLS.new(smart)
game.play while true
