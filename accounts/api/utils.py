import random
import string


def code_slug_generator(size=6, chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def create_activation_code(size, model_):
    new_code = code_slug_generator(size=size)
    qs_exists = model_.objects.filter(activation_code=new_code).exists()
    return create_activation_code(size, model_) if qs_exists else new_code