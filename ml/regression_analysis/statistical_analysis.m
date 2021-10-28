% Get car_data from data processing script
run data_processing;

%-----------------------------------------------------
% Calculate the data statistics
%-----------------------------------------------------
% Columns (4): MPG, horsepower, weight, acceleration
mpg = {};
hp = {};
wgt = {};
acc = {};

% Loop through column data
for c = 1:size(car_data, 2)-3 % 6
    % Set col data
    col_data = table2array(car_data(:, c));
    
    % Only get the four columns we need
    if c == 1
      % Create row of stats for mpg column
      mpg = calc_stats(col_data, 'mpg');      
    end
    if c == 4
        % Create row of stats for horsepower column
        hp = calc_stats(col_data, 'horsepower');
    end
    if c == 5
        % Create row of stats for weight column
        wgt = calc_stats(col_data, 'weight');
    end
    if c == 6
        % Create row of stats for acceleration column
        acc = calc_stats(col_data, 'acceleration');
    end
end

% Create a table of statistics
statistics = table();
stats_headers = {'variable', 'mean', 'median', 'min', 'max', 'std'};
statistics = [statistics; mpg; hp; wgt; acc];
statistics.Properties.VariableNames = stats_headers;

% Create correlations matrix table
col_names = {'MPG', 'Horsepower', 'Weight', 'Acceleration'};
col_data = [car_data.MPG, car_data.horsepower, car_data.weight, car_data.acceleration];
corr_table = create_corr_matrix(col_names, col_data);

% Remove unneeded workspace variables
clear ans c mpg hp wgt acc data_size stats_headers col_data;

%-----------------------------------------------------
% Custom Functions
%-----------------------------------------------------
% Create calc_stats function
function s = calc_stats(data, name)
    % Check is correct column
    mean = calc_mean(data);
    median = calc_median(data);
    min = calc_min(data);
    max = calc_max(data);
    std = calc_std(data, mean);

    % Create and return cell row
    s = {name, mean, median, min, max, std};
end

% Create create_corr_matrix function
function cm_rows = create_corr_matrix(names, data)
    all_cols = [];
    % Create rows equal to length of column names
    for n = 1:length(names)
        col = [];
        % Loop through each column of data
        for c = 1:length(names)
            corr = calc_correlation(data(:, n), data(:, c));
            col = [col; corr];
        end
        all_cols = [all_cols, col];
    end
    % Create correlation matrix
    cm_rows = array2table(all_cols, 'VariableNames', names, 'RowNames', names);
end

% Create calc_correlation function
function corr = calc_correlation(x, y)
    % Calculate both column means
    x_mean = calc_mean(x);
    y_mean = calc_mean(y);
   
    % Initialize variables for fraction equation 
    numerator = 0;
    denom_x = 0;
    denom_y = 0;
     
    % Loop through each value
    for d = 1:size(x, 1)
        % Calculate new values
        new_x = (x(d) - x_mean);
        new_y = (y(d) - y_mean);
        
        % Calculate numerator and denominator components
        numerator = numerator + (new_x * new_y);
        denom_x = denom_x + (new_x * new_x);
        denom_y = denom_y + (new_y * new_y);
    end
    
    % Calculate Pearsons correlation coefficient
    denominator = denom_x * denom_y;
    corr = numerator / (denominator ^ 0.5);
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

% Create calc_median function
function med = calc_median(data)
    % Sort data into ascending order
    s_data = bubble_sort(data);
    
    % Find middle point
    mid_val = size(s_data, 1) ./ 2;
    if mod(size(s_data, 1), 2) == 0 
        % Add left and right values, divide by 2
        l_val = s_data(mid_val);
        r_val = s_data(mid_val+1);
        
        % Calculate median
        med = (l_val + r_val) ./ 2;
    else
        med = s_data(mid_val);
    end
end

% Create bubble_sort function
function s = bubble_sort(data)
    swapped = true;
    % Loop through each item of data
    while swapped
        swapped = false;
        % Swap elements
        for ele = 1:size(data)-1
            % Swap element if greater than next
            if data(ele) > data(ele+1)
                temp = data(ele);
                data(ele) = data(ele+1);
                data(ele+1) = temp;
                swapped = true;
            end
        end
    end
    s = data;
end

% Create calc_min function
function min = calc_min(data)
    min = data(1);
    % loop through each item of data
    for num = 2:size(data, 1)
        % If num is less than current val
        if data(num) < min
            % Set as new min
            min = data(num);
        end
    end
end

% Create calc_max function
function max = calc_max(data)
    max = data(1);
    % loop through each item of data
    for num = 2:size(data, 1)
        % If num is greater than current val
        if data(num) > max
            % Set as new max
            max = data(num);
        end
    end  
end

% Create calc_std function
function std = calc_std(data, mean)
    row_count = size(data, 1);
    total = 0;
    % Loop through each item of data
    for num = 1:row_count
       % Formula: sqrt(sum((col_item - mean)^2) / row_count)
       total = total + ((data(num) - mean).^2);
    end
    std = (total ./ row_count)^ 0.5;
end

