# A Python-Based Maze Solver
This program allows you to import text-based mazes and have an agent solve them using various path-find algorithms. 
The agent will start at the capital S in the text file and attempt to reach the capital G in the text file. Spaces
represent valid walkable space for the agent and percentage characters "%" represent walls. The program will also
display data about how many nodes were expanded to find the solution, and the total cost of the solution.

To run this file, do the following:

```search.py -method [PATH FINDING METHOD] [NAME OF TEXT FILE]```

```[PATH FINDING METHOD]``` should be replaced with one the following arguments.

| Argument      | Description                       |
| :---:         |    :----:                         |
| astar         | A* Search Algorithm               |
| depth         | Depth-first Search Algorithm      |
| breadth       | Breadth-first Search Algorithm    |

```[NAME OF TEXT FILE]``` should be replaced with the name of the text file. Be sure to include the extension.

A valid example of a command to run this file could look like the following: ```search.py -method astar Maze1.txt```

Included in this repository are three different example maze text files that are all solveable by the agent.

## Example Of Agent In-Action
The following is an example input and output of the agent solving Maze1.txt.

**INPUT MAZE**
```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     %       %             %         %     %           %   %
%%% %%% %%%%%   %%%%% %%%%% %%% %%%%%%% % %%% %%%%%%%%%%% %%%
%   %   %     %   % %   % %   %         %          % % %    %
% %%% %%% %%% %%% % %%% % %%% % %%%%%% %%%%% %%%%% % % %%%% %
% %   % %   % %   %   % % % % %     %        %   % % %      %
%   %%% % % % % % % % %%% % % % %%% % %%%% % %%% % % %% % % %
% %   %   % %   %   % %   % %     % % %  % %     % %  %%% % %
% %%%%%%% % % %%% %%% %%%   %%% %%% % % %% %%%%% %%%% % % % %
%   %   % %       % % %   % % %  %  % %  %    %     %   % % %
% % %%% % %%%%%%%%% % % %%% % %  % %% %% % %%%%%%%%%%% %%%% %
% %   % %   %       %%% %     %  %    %  %      %           %
% % %%% %%%%% %%%%%   % %%%%%%%% %%% %%% % %% %%% %%%%%%% % %
% %   %       %     %   %        %     % %  %   %     %   % %
% %%%%%%% %%%%% %%%%% % %%%%% %%%%%%%%%% % %%%%%% %%% %%% % %
% % %     %     %   % %             %    %    %   %     % % %
%   %%% %%% %%%%%%% %%%%% %%%%%%% %%% %% %%%  % %%% %%% %%% %
% %   %   %       % %     %            %   %    %     %   % %
% %%%%% % %%%%%%% %%%%%%% %%%%%%%% %%% % %%%%%% % % %%%%% % %
%G%     %   %     %       %   %    %   %        % % %   % % %
%%%%%% %% % % %%%%% %%%%% %%% % %%%% %%%%%%%%%%%%%%%% %%% % %
%S        % %           %     %           %           %     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

**OUTPUT SOLVED MAZE**
```
Size of Maze: 61 x 23
Start Coordinates: (1, 21)

A* Search has found G at (1, 19)
Number of expanded nodes: 275
Total Cost: 110
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     %•••••••%•••••••••••••%         %     %           %   %
%%% %%%•%%%%%•••%%%%% %%%%%•%%% %%%%%%% % %%% %%%%%%%%%%% %%%
%   %•••%     %   % %   % %•••%         %          % % %    %
% %%%•%%% %%% %%% % %%% % %%%•% %%%%%% %%%%% %%%%% % % %%%% %
% %•••% %   % %   %   % % % %•%     %        %   % % %      %
%•••%%% % % % % % % % %%% % %•% %%% % %%%% % %%% % % %% % % %
%•%   %   % %   %   % %   % %•••  % % %  % %     % %  %%% % %
%•%%%%%%% % % %%% %%% %%%   %%%•%%% % % %% %%%%% %%%% % % % %
%•  %   % %       % % %   % % %• %  % %  %    %     %   % % %
%•% %%% % %%%%%%%%% % % %%% % %• % %% %% % %%%%%%%%%%% %%%% %
%•%   % %   %•••••••%%% %     %••%    %  %      %           %
%•% %%% %%%%%•%%%%%•••% %%%%%%%%•%%% %%% % %% %%% %%%%%%% % %
%•%   %  •••••%     %•••%    ••••%     % %  %   %     %   % %
%•%%%%%%%•%%%%% %%%%% %•%%%%%•%%%%%%%%%% % %%%%%% %%% %%% % %
%•% %  •••%     %   % %•••••••      %    %    %   %     % % %
%•  %%%•%%% %%%%%%% %%%%% %%%%%%% %%% %% %%%  % %%% %%% %%% %
%•%   %•  %       % %     %            %   %    %     %   % %
%•%%%%%•% %%%%%%% %%%%%%% %%%%%%%% %%% % %%%%%% % % %%%%% % %
%G%   ••%   %     %       %   %    %   %        % % %   % % %
%%%%%%•%% % % %%%%% %%%%% %%% % %%%% %%%%%%%%%%%%%%%% %%% % %
%S•••••   % %           %     %           %           %     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```
