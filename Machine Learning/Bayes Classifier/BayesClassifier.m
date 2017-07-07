
function prediction = BayesClassifier(X, y, X_test)

[n,d] = size(X);
K = unique(y);
c = size(K);
prior = zeros(d,1);
mu = zeros(c,d);
Sigma = zeros(d,d,c);
test_n = size(X_test,1);
prediction = zeros(test_n,c);

for i = 0:c-1
    ind = y(:) == i;
    X_k = X(ind,:);
    len = size(X_k,1);
    prior(i+1) = len/n;
    mu(i+1,:) = sum(X_k)/len;
    Sigma(:,:,i+1) = ((X_k-mu(i+1,:)).') * (X_k-mu(i+1,:));
    Sigma(:,:,i+1) = Sigma(:,:,i+1)/len;
end

for i = 1:test_n
    x_i = X_test(i,:);
    for j = 1:c
        part1 = prior(j)/sqrt(det(Sigma(:,:,j)));
        part2 = exp((-1/2) *  (x_i - mu(j,:))* inv(Sigma(:,:,j)) *((x_i - mu(j,:)).'));
        prediction(i,j) = part1 * part2;
    end
end

end