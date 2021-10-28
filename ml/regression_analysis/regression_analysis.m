mul% Get the data and statistical information from script
run statistical_analysis;

%-----------------------------------------------------
% Perform Regression Analysis
%-----------------------------------------------------
% Regression 1: Acceleration vs MPG (Training Data)
[x_train1, x_test1, y_train1, y_test1] = split_data(car_data.acceleration, car_data.MPG, 0.3); % 122 test, 284 train
y_pred_train1 = linear_regression(x_train1, y_train1);
error_train1 = mean_squared_error(y_train1, y_pred_train1);

% Regression 2: Horsepower vs MPG (Training Data)
[x_train2, x_test2, y_train2, y_test2] = split_data(car_data.horsepower, car_data.MPG, 0.3); % 122 test, 284 train
y_pred_train2 = linear_regression(x_train2, y_train2);
error_train2 = mean_squared_error(y_train2, y_pred_train2);

% Regression 3: Weight vs Horsepower (Training Data)
[x_train3, x_test3, y_train3, y_test3] = split_data(car_data.weight, car_data.horsepower, 0.3); % 122 test, 284 train
y_pred_train3 = linear_regression(x_train3, y_train3);
error_train3 = mean_squared_error(y_train3, y_pred_train3);

%-----------------------------------------------------
% Evaluate Regression Models
%-----------------------------------------------------
% Regression 1: Acceleration vs MPG (Testing Data)
y_pred_test1 = linear_regression(x_test1, y_test1);
error_test1 = mean_squared_error(y_test1, y_pred_test1);

% Regression 2: Horsepower vs MPG (Testing Data)
y_pred_test2 = linear_regression(x_test2, y_test2);
error_test2 = mean_squared_error(y_test2, y_pred_test2);

% Regression 3: Weight vs Horsepower (Testing Data)
y_pred_test3 = linear_regression(x_test3, y_test3);
error_test3 = mean_squared_error(y_test3, y_pred_test3);

% Set plot colours
blue = [0.2, 0.2, 0.8];
red = [0, 0.8, 0.1];
green = [0.8, 0, 0.1];

% Plot graphs
lr_plot(x_test1, y_test1, y_pred_test1, 'Acceleration', 'MPG', 'Acceleration vs MPG', 'lr_acc_vs_mpg', blue);
lr_plot(x_test2, y_test2, y_pred_test2, 'Horsepower', 'MPG', 'Horsepower vs MPG', 'lr_hp_vs_mpg', red);
lr_plot(x_test3, y_test3, y_pred_test3, 'Weight', 'Horsepower', 'Weight vs Horsepower', 'lr_w_vs_hp', green);

% Create error table for easy readability and comparison
error_table = table();
error_headings = {'Acceleration vs MPG', 'Horsepower vs MPG', 'Weight vs Horsepower'};
error_data = [error_train1, error_train2, error_train3; error_test1, error_test2, error_test3];
error_table = array2table(error_data, 'VariableNames', error_headings, 'RowNames', {'Training', 'Testing'});

% Remove unneeded workspace variables
clear blue red green error_data error_headings error_test1 error_test2 error_test3 error_train1 error_train2 error_train3;

%-----------------------------------------------------
% Custom Functions
%-----------------------------------------------------
% Create split_data function
function [x_train, x_test, y_train, y_test] = split_data(x, y, split_rate)
    % Calculate test quantity
    test_total = round(numel(x) * split_rate);
    
    % Randomly select testing data idxs
    rng(1); % Set seed for recreation purposes
    test_idxs = randperm(length(x), test_total).';
    
    % Set test dataset values
    x_test = x(test_idxs);
    y_test = y(test_idxs);
    
    % Create list of indexes
    train_idxs = [];
    for i = 1:size(x, 1)
        train_idxs = [train_idxs; i];
    end
    
    % Remove test indexes
    train_idxs = setdiff(train_idxs, test_idxs);
    
    % Set training dataset values
    x_train = x(train_idxs); 
    y_train = y(train_idxs);
end

% Create linear_regression function
function y_pred = linear_regression(x, y)
    % Formula: y = w0 + w1 * x
    % Calculate slope using LLS and the y-intercept
    w1 = linear_least_squares(x, y); % slope
    w0 = calc_mean(y) - (w1 * calc_mean(x)); % y_intercept
    y_pred = w0 + (w1 * x);
end

% Create linear_least_squares function
function lls = linear_least_squares(x, y)
    % Formula: w = sum((x - mean(x)) * (y - mean(y))) / sum((x - mean(x) ^ 2))
    % Create equation components
    denominator = 0;
    numerator = 0;
    
    % Loop through each item
    for i = 1:length(x)
        new_x = (x(i) - calc_mean(x));
        new_y = (y(i) - calc_mean(y));
        numerator = numerator + (new_x * new_y);
        denominator = denominator + (new_x ^ 2);
    end
    
    % Calculate slope
    lls = numerator / denominator;
end

% Create mean_squared_error function
function mse = mean_squared_error(y, y_pred)
    % Formula: mean(sum((y - y_pred)^2))
    N = length(y);
    total = 0;
    
    % Loop through each item
    for item = 1:N
        % Calculate the total
        total = total + ((y(item) - y_pred(item)) ^ 2);
    end
    mse = total / N;
end

% Create lr_plot function
function lr_plot(x, y, y_pred, x_label, y_label, plot_title, plot_name, colour)
    % Plot figure
    f = figure('Position', [200, 200, 1000, 800]);
    scatter(x, y, 'filled', 'MarkerFaceColor', colour, 'MarkerEdgeColor', 'k');
    hold on
    plot(x, y_pred, 'LineWidth', 2, 'Color', [1, 0.6, 0]);
    hold off
    xlabel(x_label);
    ylabel(y_label);
    title(plot_title);
    saveas(f, join(['plots/', plot_name]), 'png');
end

% Create calc_mean function
function mean = calc_mean(data)
    row_count = size(data, 1);
    col_total = 0;
    % Calculate each columns total
    for d = 1:row_count
        col_total = col_total + data(d);
    end
    mean = col_total ./ row_count;
end
