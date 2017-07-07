
function Wrr = RidgeRegression(X,y,lambda)
reg = eye(size(X,2));
reg(1:end-1,:) = lambda * reg(1:end-1,:);
Wrr = inv(reg + ((X.') * X)) * (X.') * y;

end
