% Reset workspace variables
clear;

%----------------------------------------------
% Load Data From File
%----------------------------------------------
% Open data file
file_id = fopen('car_data.csv', 'r');

% Get headers
headers = strsplit(fscanf(file_id, '%s', 1), ',');

% Get data line by line
line = fgetl(file_id);
while ischar(line)
    data = fscanf(file_id, '%c', Inf); % Character array
    line = fgetl(file_id); % Go to next line
end

% Close data file
fclose(file_id);

% Convert to string and split into columns
data = string(splitlines(data));

car_data = table(); % Set initial table variable
% Loop through each row of data
for i = 1:size(data)
    % Split rows into columns
    tmp = cellstr(strsplit(data(i), ','));    
    
    % Ignore empty table rows
    if tmp ~= ""
        % Add data as column rows to table
        car_data = [car_data; tmp];
    end
end

% Set header names and change data types
car_data.Properties.VariableNames = headers;

% Check data size
data_size = size(car_data); % [406, 9]

% Change table data types
car_data.MPG = str2double(cellstr(car_data.MPG));
car_data.cylinders = str2double(cellstr(car_data.cylinders));
car_data.displacement = str2double(cellstr(car_data.displacement));
car_data.horsepower = str2double(cellstr(car_data.horsepower));
car_data.weight = str2double(cellstr(car_data.weight));
car_data.acceleration = str2double(cellstr(car_data.acceleration));
car_data.modelYear = str2double(cellstr(car_data.modelYear));
car_data.origin = str2double(cellstr(car_data.origin));
car_data.carName = cellstr(car_data.carName);

% Remove unneeded variables
clear file_id line data i tmp ans;

%----------------------------------------------
% Handle missing data
%----------------------------------------------
% Get row count, ignoring NA values for col 1 and 4
c1_count = ignore_missing(car_data.MPG);
c4_count = ignore_missing(car_data.horsepower);

% Calculate mean for missing data (in cols 1 and 4)
c1_mean = calc_mean(car_data.MPG, c1_count);
c4_mean = calc_mean(car_data.horsepower, c4_count);

% Replace NA values with mean values
for r = 1:size(car_data, 1)
   % Get each item as a cell to check for NA
   % First column
   if isnan(car_data.MPG(r))
       car_data.MPG(r) = c1_mean;
   end
   % Fourth column
   if isnan(car_data.horsepower(r))
       car_data.horsepower(r) = c4_mean;
   end
end

% Remove unneeded variables
clear row_count r c1_mean c4_mean c1_count c4_count m;

%----------------------------------------------
% Custom Functions
%----------------------------------------------
% Create calc_mean function
function m = calc_mean(data, row_count)
    col_total = 0;
    % Calculate each columns total
    for d = 1:size(data, 1)
        if ~isnan(data(d))
            col_total = col_total + data(d);
        end
    end
    m = col_total ./ row_count;
end

% Create ignore_missing function
function count = ignore_missing(data)
    count = 0;
    % Loop through each data point
    for i = 1:size(data, 1)
        % Check value isn't NA
        if ~isnan(data(i))
            % Add count + 1
            count = count + 1;
        end
    end
end
