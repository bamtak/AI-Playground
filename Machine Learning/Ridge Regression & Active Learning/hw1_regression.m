
%% Initialization
clear ; close all; clc

arg_lst = argv();
lambda = str2double(arg_lst{1})
sigma2 = str2double(arg_lst{2});
X_train = load(arg_lst{3});
y = load(arg_lst{4});
X_test = load(arg_lst{5});
output_wrr = ['wRR_' arg_lst{1} '.csv'];
output_al = ['active_' arg_lst{1} '_' arg_lst{2} '.csv'];

wrr = RidgeRegression(X_train,y,lambda);
x = ActiveLearning(X_train,lambda,sigma2,X_test);

csvwrite(output_wrr,wrr);
csvwrite(output_al,x);
