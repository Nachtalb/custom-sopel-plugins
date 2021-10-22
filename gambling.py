from sopel import plugin, tools
from sopel.formatting import italic
from datetime import datetime, timedelta
import random
import sqlite3
import time
import unicodedata


@plugin.require_admin
@plugin.require_chanmsg
@plugin.command("award")
def award_money(bot, trigger):
    """Bot admin uses the power of Admin Abuse to spawn money from nothing."""
    if trigger.sender == "#casino":
        try:
            amount = int(trigger.group(3).replace(",", "").replace("$", ""))
            winner = trigger.group(4)
        except AttributeError:
            bot.reply("I need an amount and a target.")
            return
        except TypeError:
            bot.reply("I need an amount of money to award.")
            return
        except ValueError:
            bot.reply("That's not a number...")
            return

        if not (winner and amount):
            bot.reply("I need an amount and a target.")
            return

        # Check for valid target to award money to.
        winner = tools.Identifier(winner)
        if winner not in bot.channels[trigger.sender].users:
            bot.reply("Please provide a valid user.")
            return

        award_amount = bot.db.get_nick_value(
            winner, "currency_amount", 0) + amount
        bot.db.set_nick_value(winner, "currency_amount", award_amount)
        bot.say("{} has ${:,}".format(winner, award_amount))
    else:
        bot.reply("This command can only be used in #casino")


@plugin.require_admin
@plugin.require_chanmsg
@plugin.command("take")
def take_money(bot, trigger):
    """Bot admin takes (deletes) X amount of money from a user."""
    if trigger.sender == "#casino":
        try:
            amount = int(trigger.group(3).replace(",", "").replace("$", ""))
            loser = trigger.group(4)
        except AttributeError:
            bot.reply("I need an amount and a target.")
            return
        except TypeError:
            bot.reply("I need an amount of money to take.")
            return
        except ValueError:
            bot.reply("That's not a number...")
            return

        if not (loser and amount):
            bot.reply("I need an amount and a target.")
            return

        # Check for valid target to take money from.
        loser = tools.Identifier(loser)
        if loser not in bot.channels[trigger.sender].users:
            bot.reply("Please provide a valid user.")
            return

        take_amount = bot.db.get_nick_value(
            loser, "currency_amount", 0) - amount
        bot.db.set_nick_value(loser, "currency_amount", take_amount)
        bot.say("{} has ${:,}".format(loser, take_amount))
    else:
        bot.reply("This command can only be used in #casino")


@plugin.require_chanmsg
@plugin.command("give")
def give_money(bot, trigger):
    """Give X amount of your money to another user."""
    if trigger.sender == "#casino":
        giver = trigger.nick
        try:
            amount = int(trigger.group(3).replace(",", "").replace("$", ""))
            target = trigger.group(4)
        except AttributeError:
            bot.reply("I need an amount and a target.")
            return
        except TypeError:
            bot.reply("I need an amount of money to give.")
            return
        except ValueError:
            bot.reply("That's not a number...")
            return

        if not (target and amount):
            bot.reply("I need an amount and a target.")
            return

        # Check if user has enough money to give away...
        give_check = bot.db.get_nick_value(giver, "currency_amount")
        if give_check is None:
            bot.reply(
                "You don't have any money to give away. Please run the `.iwantmoney` command.")
            return
        if amount > give_check:
            bot.reply(
                "You don't have that much money to give away. Try a smaller amount.")
            return
        if amount <= 0:
            bot.reply("Giving away nothing is pretty scummy. :(")
            return

        # Check for valid target to give money to.
        target = tools.Identifier(target)
        if target not in bot.channels[trigger.sender].users:
            bot.reply("Please provide a valid user.")
            return

        give_amount = bot.db.get_nick_value(
            giver, "currency_amount", 0) - amount
        receive_amount = bot.db.get_nick_value(
            target, "currency_amount", 0) + amount
        # Take away the money from the giver.
        bot.db.set_nick_value(giver, "currency_amount", give_amount)
        # Give the money to the target/reciever.
        bot.db.set_nick_value(target, "currency_amount", receive_amount)
        bot.say(
            "{} gifted ${:,} to {}. {} now has ${:,} and {} has ${:,}.".format(
                giver,
                amount,
                target,
                giver,
                give_amount,
                target,
                receive_amount))
    else:
        bot.reply("This command can only be used in #casino")


@plugin.require_admin
@plugin.command("nomoremoney")
def delete_money(bot, trigger):
    """Bot admin can make it so a user never had any money."""
    target = trigger.group(3)

    if not target:
        bot.reply("I need someone's wealth to eliminate.")
        return

    bot.db.delete_nick_value(target, "currency_amount")
    bot.say("{}'s wealth has been deleted from existence.".format(target))


@plugin.require_chanmsg
@plugin.command(r"\$")
def check_money(bot, trigger):
    """Check how much money you or another user has."""
    if trigger.sender == "#casino":
        target = trigger.group(3) or trigger.nick

        if not target:
            bot.reply("How in the hell did you do this?")
            return

        currency_amount = bot.db.get_nick_value(target, "currency_amount")
        if currency_amount is not None:
            bot.say("{} has ${:,}".format(target, currency_amount))
        else:
            bot.say(
                "{} has never participated in the currency plugin.".format(target))
    else:
        bot.reply("This command can only be used in #casino")


@plugin.require_chanmsg
@plugin.command("iwantmoney")
def init_money(bot, trigger):
    """Use this command to get money for the first time ever and participate in gambling and other fun activities!"""
    if trigger.sender == "#casino":
        target = trigger.nick
        check_for_money = bot.db.get_nick_value(target, "currency_amount")
        if check_for_money is None:
            bot.db.set_nick_value(target, "currency_amount", 100)
            bot.say(
                "Congratulations! Here's $100 to get you started, {}.".format(target))
    else:
        bot.reply("This command can only be used in #casino")


@plugin.require_chanmsg  # Forcing public claiming serves as a reminder to all.
@plugin.command("timely")
def claim_money(bot, trigger):
    """Claim $10 every hour. ($100 for first claim!)"""
    if trigger.sender == "#casino":
        claimer = trigger.nick

        check_for_money = bot.db.get_nick_value(claimer, "currency_amount")
        if check_for_money is None:
            bot.say("You can't do this yet! Please run the `.iwantmoney` command.")
            return

        now = time.time()

        check_for_timely = bot.db.get_nick_value(claimer, "currency_timely")
        if check_for_timely is None:
            bot.db.set_nick_value(claimer, "currency_timely", now)
            claim = check_for_money + 100
            bot.db.set_nick_value(claimer, "currency_amount", claim)
            bot.reply(
                "New balance: ${:,}. Don't forget to claim again in an hour! ($10/hr going forward.)".format(claim))
            return

        check_1_hour = now - check_for_timely
        if check_1_hour >= 3600:
            bot.db.set_nick_value(claimer, "currency_timely", now)
            claim = check_for_money + 10
            bot.db.set_nick_value(claimer, "currency_amount", claim)
            bot.reply(
                "New balance: ${:,}. Don't forget to claim again in an hour!".format(claim))
            return
        else:
            to_1_hour = 3600 - check_1_hour
            time_remaining = str(timedelta(seconds=round(to_1_hour)))
            bot.reply(
                "{} until you can claim again, greedy!".format(time_remaining))
    else:
        bot.reply("This command can only be used in #casino")


@plugin.require_admin
@plugin.command("timelyreset")
def timely_reset(bot, trigger):
    """Reset a user's timely timer for whatever reason."""
    target = trigger.group(3)

    if not target:
        bot.reply("I need someone's timely timer to reset.")
        return

    target = tools.Identifier(target)

    bot.db.delete_nick_value(target, "currency_timely")
    bot.say("{}'s timely timer has been reset.".format(target))


@plugin.command("betflip", "bf")
@plugin.example(".bf 10 h")
def gamble_betflip(bot, trigger):
    """Wager X amount of money on (h)eads or (t)ails. Winning will net you double your bet."""
    if trigger.sender == "#casino":
        gambler = trigger.nick
        # Check that user has actually gambled some amount of money.
        try:
            bet = int(trigger.group(3).replace(",", "").replace("$", ""))
        except AttributeError:
            bot.reply("I need an amount of money to bet and (h)eads or (t)ails.")
            return plugin.NOLIMIT
        except TypeError:
            bot.reply("I need an amount of money to bet.")
            return plugin.NOLIMIT
        except ValueError:
            bot.reply("That's not a number...")
            return plugin.NOLIMIT

        # Check if user has enough money to make the gamble...
        bet_check = bot.db.get_nick_value(gambler, "currency_amount")
        if bet_check is None:
            bot.reply(
                "You can't gamble yet! Please run the `.iwantmoney` command.")
            return plugin.NOLIMIT
        if bet > bet_check:
            bot.reply(
                "You don't have enough money to make this bet. Try a smaller bet.")
            return plugin.NOLIMIT
        if bet <= 0:
            bot.reply("You can't bet nothing!")
            return plugin.NOLIMIT

        # Check if user has actually bet (H)eads or (T)ails.
        user_choice = trigger.group(4)
        if user_choice in ["h", "t", "heads", "tails"]:

            heads_or_tails = ["heads", "tails"]

            if user_choice == "h":
                user_choice = "heads"

            if user_choice == "t":
                user_choice = "tails"

            # Flip coin and keep the gambler in suspense...
            flip_result = random.choice(heads_or_tails)
            bot.action("flips a coin...")
            time.sleep(1.5)

            if flip_result == user_choice:
                winnings = bet * 2
                new_balance = bet_check + bet
                bot.db.set_nick_value(
                    gambler, "currency_amount", new_balance)
                bot.reply(
                    "Congrats; the coin landed on {}. You won ${:,}! Your new balance is ${:,}.".format(
                        flip_result, winnings, new_balance))
                return
            else:
                new_balance = bet_check - bet
                bot.db.set_nick_value(
                    gambler, "currency_amount", new_balance)
                bot.reply(
                    "Sorry, the coin landed on {}. You lost ${:,}. Your new balance is ${:,}.".format(
                        flip_result, bet, new_balance))
                return
        else:
            bot.reply("I need you to bet on (h)eads or (t)ails.")
    else:
        bot.reply("This command can only be used in #casino")


@plugin.command("br", "betroll")
@plugin.example(".br 200")
def gamble_betroll(bot, trigger):
    """Bet your money on a random roll from 0-100. Roll payouts:
    0-66: 0x // 67-90: 2x // 91-99: 4x // 100: 10x"""
    if trigger.sender == "#casino":
        gambler = trigger.nick
        # Check that user has actually gambled some amount of money.
        try:
            bet = int(trigger.group(3).replace(",", "").replace("$", ""))
        except AttributeError:
            bot.reply("I need an amount of money to bet.")
            return plugin.NOLIMIT
        except TypeError:
            bot.reply("I need an amount of money to bet.")
            return plugin.NOLIMIT
        except ValueError:
            bot.reply("That's not a number...")
            return plugin.NOLIMIT

        # Check if user has enough money to make the gamble...
        bet_check = bot.db.get_nick_value(gambler, "currency_amount")
        if bet_check is None:
            bot.reply(
                "You can't gamble yet! Please run the `.iwantmoney` command.")
            return plugin.NOLIMIT
        if bet > bet_check:
            bot.reply(
                "You don't have enough money to make this bet. Try a smaller bet.")
            return plugin.NOLIMIT
        if bet <= 0:
            bot.reply("You can't bet nothing!")
            return plugin.NOLIMIT

        # Take the user's money before continuing
        spend_on_bet = bet_check - bet
        bot.db.set_nick_value(gambler, "currency_amount", spend_on_bet)

        # Roll a number 0-100
        roll = random.randint(0, 100)
        # Determine multiplier
        if 0 <= roll <= 66:
            multiplier = 0
        elif 67 <= roll <= 90:
            multiplier = 2
        elif 91 <= roll <= 99:
            multiplier = 4
        elif roll == 100:
            multiplier = 10

        # Process winnings
        winnings = bet * multiplier
        new_balance = spend_on_bet + winnings
        bot.db.set_nick_value(gambler, "currency_amount", new_balance)

        # Stress user with delay and output result
        bot.say(italic("Rolling a number..."))
        time.sleep(1.5)

        # Conditionals
        if multiplier == 0:
            bot.reply(
                "You rolled {}. You lost. {}x multiplier. New balance: ${:,}.".format(
                    roll, multiplier, new_balance))
            return
        elif multiplier in (2, 4):
            bot.reply(
                "You rolled {}. You win! {}x multiplier. New balance: ${:,}.".format(
                    roll, multiplier, new_balance))
            return
        elif multiplier == 10:
            bot.reply(
                "🎊 Holy shit! You rolled a {} which means {}x multiplier! New balance: ${:,}. 🎊".format(
                    roll, multiplier, new_balance))
            return
    else:
        bot.reply("This command can only be used in #casino")


@plugin.command("oe")
@plugin.example(".oe 10 e")
def gamble_oddsevens(bot, trigger):
    """Wager X amount of money on (o)dds or (e)vens. Winning will net you double your bet."""
    if trigger.sender == "#casino":
        gambler = trigger.nick
        # Check that user has actually gambled some amount of money.
        try:
            bet = int(trigger.group(3).replace(",", "").replace("$", ""))
        except AttributeError:
            bot.reply("I need an amount of money to bet and (o)dds or (e)vens.")
            return plugin.NOLIMIT
        except TypeError:
            bot.reply("I need an amount of money to bet.")
            return plugin.NOLIMIT
        except ValueError:
            bot.reply("That's not a number...")
            return plugin.NOLIMIT

        # Check if user has enough money to make the gamble...
        bet_check = bot.db.get_nick_value(gambler, "currency_amount")
        if bet_check is None:
            bot.reply(
                "You can't gamble yet! Please run the `.iwantmoney` command.")
            return plugin.NOLIMIT
        if bet > bet_check:
            bot.reply(
                "You don't have enough money to make this bet. Try a smaller bet.")
            return plugin.NOLIMIT
        if bet <= 0:
            bot.reply("You can't bet nothing!")
            return plugin.NOLIMIT

        # Check if user has actually bet (o)dds or (e)vens.
        user_choice = trigger.group(4)
        if user_choice in ["o", "e", "odd", "even", "odds", "evens"]:

            if user_choice == "odd":
                pass
            elif user_choice == "o" or user_choice == "odds":
                user_choice = "odd"
            elif user_choice == "even":
                pass
            elif user_choice == "e" or user_choice == "evens":
                user_choice = "even"

            # Roll the number, check if even or odd
            roll_num = random.randint(0, 100)
            if (roll_num % 2) == 0:
                roll = "even"
            else:
                roll = "odd"

            # Calculate winning and such
            if roll == user_choice:
                winnings = bet * 2
                new_balance = bet_check + bet
                bot.db.set_nick_value(gambler, "currency_amount", new_balance)
                bot.action("rolls a number...")
                time.sleep(1.5)
                bot.reply(
                    "I rolled {}. That's {}. You bet on {}. You won ${:,}! Your new balance is ${:,}.".format(
                        roll_num, roll, user_choice, winnings, new_balance))
                return
            else:
                new_balance = bet_check - bet
                bot.db.set_nick_value(gambler, "currency_amount", new_balance)
                bot.action("rolls a number...")
                time.sleep(1.5)
                bot.reply(
                    "I rolled {}. That's {}. You bet on {}. You lost ${:,}. Your new balance is ${:,}.".format(
                        roll_num, roll, user_choice, bet, new_balance))
                return
        else:
            bot.reply("I need you to bet on (o)dds or (e)vens.")
    else:
        bot.reply("This command can only be used in #casino")


@plugin.command("wheeloffortune", "wheel")
@plugin.example(".wheel 100")
def gamble_wheel(bot, trigger):
    """Spin the Wheel of Fortune!"""
    if trigger.sender == "#casino":
        gambler = trigger.nick
        # Check that user has actually gambled some amount of money.
        try:
            bet = int(trigger.group(3).replace(",", "").replace("$", ""))
        except AttributeError:
            bot.reply("I need an amount of money to bet.")
            return plugin.NOLIMIT
        except TypeError:
            bot.reply("I need an amount of money to bet.")
            return plugin.NOLIMIT
        except ValueError:
            bot.reply("That's not a number...")
            return plugin.NOLIMIT

        # Check if user has enough money to make the gamble...
        bet_check = bot.db.get_nick_value(gambler, "currency_amount")
        if bet_check is None:
            bot.reply(
                "You can't gamble yet! Please run the `.iwantmoney` command.")
            return plugin.NOLIMIT
        if bet > bet_check:
            bot.reply(
                "You don't have enough money to make this bet. Try a smaller bet.")
            return plugin.NOLIMIT
        if bet <= 0:
            bot.reply("You can't bet nothing!")
            return plugin.NOLIMIT

        # Take the user's money before continuing
        spend_on_bet = bet_check - bet
        bot.db.set_nick_value(gambler, "currency_amount", spend_on_bet)

        # Configure Wheel Spin Directions
        wheel_direction = ["֎", "֍"]
        pointer_direction = {
            "↗": 7,
            "→": 6,
            "↘": 5,
            "↓": 4,
            "↙": 3,
            "←": 2,
            "↖": 1,
            "↑": 0
        }

        # Get the result first
        wheel_result = random.choices(list(pointer_direction.keys()), weights=[
                                      0.1, 0.4, 0.5, 1, 3, 25, 30, 40], k=1)[0]
        multiplier = pointer_direction[wheel_result]
        winnings = bet * multiplier
        new_balance = spend_on_bet + winnings
        bot.db.set_nick_value(gambler, "currency_amount", new_balance)
        # Stress out the user with delay 😉
        bot.action(
            "spins the wheel...{0}{0}{0}".format(
                random.choice(wheel_direction)))
        time.sleep(4)
        bot.say(italic("The wheel slows to a stop..."))
        time.sleep(2)

        # Conditionals
        if multiplier == 0:
            bot.reply(
                "The arrow is facing [{}]. {}x multiplier. You lost. New balance: ${:,}.".format(
                    wheel_result, multiplier, new_balance))
            return
        elif multiplier == 1:
            bot.reply(
                "The arrow is facing [{}]. {}x multiplier. Same balance: ${:,}.".format(
                    wheel_result, multiplier, bet_check))
            return
        else:
            bot.reply(
                "The arrow is facing [{}]. You won: {}x your money! (${:,}). Your new balance is: ${:,}.".format(
                    wheel_result,
                    multiplier,
                    winnings,
                    new_balance))
    else:
        bot.reply("This command can only be used in #casino")


@plugin.command("lb")
@plugin.rate(user=5)
@plugin.require_chanmsg
def gamble_leadboard(bot, trigger):
    """Posts the top 5 richest gamblers."""
    if trigger.sender == "#casino":
        try:
            # Connect to DB
            con = sqlite3.connect("/home/xnaas/sackbot2/sopel/default.db")

            # Create whatever the fuck a cursor is
            cur = con.cursor()

            # SQL Query
            cur.execute("SELECT canonical, key, value FROM nick_values a join nicknames b on a.nick_id = b.nick_id WHERE key='currency_amount' ORDER BY cast(value as int) DESC;")

            # Store results
            lb_base = cur.fetchall()

            # Close db connection
            con.close()
        except sqlite3.OperationalError:
            bot.reply(
                "Error querying database...most likely no one has gambled yet. Try `.iwantmoney` to get started.")
            return

        # Print results
        for index, person in enumerate(lb_base):
            # Rank/Index required to actually go through data
            rank = index + 1

            # If rank 1 has $0, then no one has anything
            if rank == 1 and int(person[2]) == 0:
                bot.say("Ain't nobody got shit!")
                return

            # If a user has $0, they don't belong on the leaderboard
            if int(person[2]) == 0:
                pass
            else:
                bot.say(
                    "{}. {}: ${:,}.".format(
                        rank, "\u200B".join(
                            person[0]), int(
                            person[2])))

            # We only want to print up to 5 people
            if rank == 5:
                break
    else:
        bot.reply("This command can only be used in #casino")
