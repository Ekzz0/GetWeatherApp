import utils

if __name__ == "__main__":
    options = utils.get_options_by_action_name(utils.Action.MAIN_MENU)
    utils.loop(options)
