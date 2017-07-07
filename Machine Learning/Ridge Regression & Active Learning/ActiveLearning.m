function x = ActiveLearning(X,lambda,sigma2,X_test)
n = size(X_test,1);
x = zeros(10,1);
reg = eye(size(X,2));
reg(1:end-1,:) = lambda * reg(1:end-1,:);

X_t = X_test;
X_v = X;

for i = 1:10
    sigma2_o = zeros(n,1);
    Sigma = inv(reg + (1/sigma2) * ((X_v.') * X_v));
    for j = 1:n
        x_o = X_t(j,:);
        sigma2_o(j) = sigma2 + x_o * Sigma * (x_o.');
    end
    [v,j] = max(sigma2_o);
    x(i) = find(ismember(X_test,X_t(j,:),'rows'));
    X_v = [X_v; X_t(j,:)];
    X_t(j,:) = [];
    n = size(X_t,1);
end

end
