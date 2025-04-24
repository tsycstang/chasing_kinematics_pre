% MATLAB version >= R2014b 

function generic_chasing_matlab
    % 初始化参数
    alpha_initial = 36; % 初始角度（度）
    theta = linspace(0, 20*pi, 2500); % 角度范围
    
    % 创建图形窗口
    fig = figure('Position', [100 100 800 800]);
    
    % 创建极坐标轴
    ax = polaraxes('Parent', fig);
    ax.Position = [0.1 0.2 0.8 0.7];
    
    % 计算初始对数螺线
    r = exp(theta * (1/tand(alpha_initial)));
    polarplot(ax, theta, r, 'LineWidth', 2);
    rlim([0 60]);
    
    % 创建滑块
    uicontrol('Style', 'slider',...
        'Position', [200 50 400 30],...
        'Min', 5, 'Max', 85,...
        'Value', alpha_initial,...
        'Callback', @updatePlot);
    
    % 更新函数
    function updatePlot(src, ~)
        current_alpha = get(src, 'Value');
        new_r = exp(theta * (1/tand(current_alpha)));
        delete(findall(fig,'Type','line'));
        polarplot(ax, theta, new_r, 'LineWidth', 2);
        rlim([0 60]);
        drawnow;
    end
end