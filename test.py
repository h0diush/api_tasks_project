def get_username(username: None, ln: None, fn: None):
    def get_ln_fn():
        if  ln:
            return 'no ln'
        if  fn:
            return 'no fn'
        if username:
            return username

    return get_ln_fn()


print(get_username('ww', 'ww', 'ww'))