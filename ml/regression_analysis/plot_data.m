% Perform statistical analysis
run statistical_analysis;

%-----------------------------------------------------
% Plot the Data
%-----------------------------------------------------

% Box Plots
%-----------------
f1 = figure(1);
set(f1, 'Position', [200, 200, 1000, 800])
% Box plot of mpg
subplot(2, 2, 1)
boxplot(car_data.MPG, 'Symbol', 'o')
title('Subplot 1: MPG')

% Box plot of acceleration
subplot(2, 2, 2)
boxplot(car_data.acceleration, 'Symbol', 'o')
title('Subplot 2: Acceleration')

% Box plot of horsepower
subplot(2, 2, 3)
boxplot(car_data.horsepower, 'Symbol', 'o')
title('Subplot 3: Horsepower')

% Box plot of weight
subplot(2, 2, 4)
boxplot(car_data.weight, 'Symbol', 'o')
title('Subplot 4: Weight')
saveas(f1, 'plots/box_plots', 'png') % Save plots

% Scatter Plots
%-----------------
% Scatter plot - acc vs mpg
f2 = figure(2);
set(f2, 'Position', [200, 200, 1000, 800])
scatter(car_data.acceleration, car_data.MPG, 'filled', 'MarkerFaceColor', [0.2, 0.2, 0.8], 'MarkerEdgeColor', 'k')
title('Acceleration vs MPG')
xlabel('Acceleration')
ylabel('MPG')
saveas(f2, 'plots/acc_vs_mpg', 'png') % Save plot

% Scatter plot - hp vs mpg
f3 = figure(3);
set(f3, 'Position', [200, 200, 1000, 800])
scatter(car_data.horsepower, car_data.MPG, 'filled', 'MarkerFaceColor', [0, 0.8, 0.1], 'MarkerEdgeColor', 'k')
title('Horsepower vs MPG')
xlabel('Horsepower')
ylabel('MPG')
saveas(f3, 'plots/hp_vs_mpg', 'png') % Save plot

% Scatter plot - w vs mpg
f4 = figure(4);
set(f4, 'Position', [200, 200, 1000, 800])
scatter(car_data.weight, car_data.horsepower, 'filled', 'MarkerFaceColor', [0.8, 0, 0.1], 'MarkerEdgeColor', 'k')
title('Weight vs Horsepower')
xlabel('Weight')
ylabel('Horsepower')
saveas(f4, 'plots/w_vs_hp', 'png') % Save plot

% Density Plots
%-----------------
f5 = figure(5);
set(f5, 'Position', [200, 200, 1000, 800])
% Density plot of mpg
subplot(2, 2, 1)
ksdensity(car_data.MPG)
title('Subplot 1: MPG')

% Density plot of acceleration
subplot(2, 2, 2)
ksdensity(car_data.acceleration)
title('Subplot 2: Acceleration')

% Density plot of horsepower
subplot(2, 2, 3)
ksdensity(car_data.horsepower)
title('Subplot 3: Horsepower')

% Density plot of weight
subplot(2, 2, 4)
ksdensity(car_data.weight)
title('Subplot 4: Weight')
saveas(f5, 'plots/density_plots', 'png') % Save plots

% Remove plot workspace variables
clear f1 f2 f3 f4 f5;
