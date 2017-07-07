
%% Initialization
clear ; close all; clc

arg_lst = argv();
X = load(arg_lst{1});
y = load(arg_lst{2});
X_test = load(arg_lst{3});

prediction = BayesClassifier(X, y, X_test);

csvwrite('probs_test.csv',prediction);
