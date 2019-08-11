import inspect


def filter_args(func, args):
	sig = inspect.signature(func)
	arg_names = [param.name for param in sig.parameters.values() if param.kind == param.POSITIONAL_OR_KEYWORD]
	filtered_dict = {arg_name: args[arg_name] for arg_name in arg_names}
	return filtered_dict
