import getopt

# Clustering Parameters
config = {
    'number_of_samples' : 1000,
    'tag_list' : ['javascript', 'python'],
    'max_body_length' : 200,
    'threshold' : 0.5,
    'print_min_size' : 2,
    'enable_question_print' : True,
    'transformer_model' : 'distilbert-base-nli-stsb-mean-tokens'
}

# n: number of samples
# t: threshold
# m: model
# p: print min size
options = "n:t:m:p:"

# nos: number os samples
# tag-list: tag list
# max-body: max body length
# model: model
# print: enable question print
# print-min-size: print min size
long_options = ["nos", "tag-list =", "th", "model", "print", "print-min-size"]

def getConfig(argumentList):
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for (currentArgument, currentValue) in arguments:
            if currentArgument.strip() in ("-n", "--nos"):
                config['number_of_samples'] = int(currentValue)
            elif currentArgument.strip() in ("-t", "--th"):
                config['threshold'] = float(currentValue)
            elif currentArgument.strip() in ("-m", "--model"):
                config['transformer_model'] = currentValue
            elif currentArgument.strip() in ("-p", "--print-min-size"):
                config['print_min_size'] = int(currentValue)
            elif currentArgument.strip() == "--tag-list":
                config['tag_list'] = list(map(str, currentValue.strip('[]').split(',')))
            elif currentArgument.strip() == "--print":
                config['enable_question_print'] = bool(currentValue)
            elif currentArgument.strip() == "--print-min-size":
                config['print_min_size'] = int(currentValue)
        return config
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        return {}