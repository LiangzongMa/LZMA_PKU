function [Path,ret]=BackTestSimulatorPath
Path=mfilename('fullpath');
i=strfind(Path,'/');
Path=Path(1:i(end));
%%       数据库文件夹
BackTestDataBasePath=[Path,'BackTestDataBase'];
if ~isdir(BackTestDataBasePath)
    mkdir(BackTestDataBasePath)
end
ret.BackTestDataBasePath=BackTestDataBasePath;
%%       回测结果Log文件夹
BackTestLogsPath=[Path,'BackTestDataBase/BackTestLogs'];
if ~isdir(BackTestLogsPath)
    mkdir(BackTestLogsPath)
end
ret.BackTestLogsPath=BackTestLogsPath;
%%       因子评估Log文件夹
BackTestReportPath=[Path,'BackTestDataBase/BackTestReport'];
if ~isdir(BackTestReportPath)
    mkdir(BackTestReportPath)
end
ret.BackTestReportPath=BackTestReportPath;
%%       AllData文件夹
AllDataPath=[Path,'BackTestDataBase/DataBase/AllData'];
if ~isdir(AllDataPath)
    mkdir(AllDataPath)
end
ret.AllDataPath=AllDataPath;
%%       衍生因子算法文件夹
FactorLibPath=[Path,'BackTestDataBase/DataBase/FactorLib'];
if ~isdir(FactorLibPath)
    mkdir(FactorLibPath)
end
ret.FactorLibPath=FactorLibPath;
%%       sdk功能算法文件夹
AlgorithmLibPath=[Path,'BackTestDataBase/DataBase/AlgorithmLib'];
if ~isdir(AlgorithmLibPath)
    mkdir(AlgorithmLibPath)
end
ret.AlgorithmLibPath=AlgorithmLibPath;
%%       基础数据存放文件夹
WindData_matPath=[Path,'BackTestDataBase/DataBase/AllData/WindData_mat'];
if ~isdir(WindData_matPath)
    mkdir(WindData_matPath)
end
ret.WindData_matPath=WindData_matPath;
%%       基础因子存放文件夹
WindFactor_matPath=[Path,'BackTestDataBase/DataBase/AllData/WindFactor_mat'];
if ~isdir(WindFactor_matPath)
    mkdir(WindFactor_matPath)
end
ret.WindFactor_matPath=WindFactor_matPath;
%%       衍生因子存放文件夹
DerivativeFactor_matPath=[Path,'BackTestDataBase/DataBase/AllData/DerivativeFactor_mat'];
if ~isdir(DerivativeFactor_matPath)
    mkdir(DerivativeFactor_matPath)
end
ret.DerivativeFactor_matPath=DerivativeFactor_matPath;
%%       基础因子（1分钟线）存放文件夹
DailyQuotes_1MPath=[Path,'BackTestDataBase/DataBase/AllData/QuoteFactor_mat/DailyQuotes_1M'];
if ~isdir(DailyQuotes_1MPath)
    mkdir(DailyQuotes_1MPath)
end
ret.DailyQuotes_1MPath=DailyQuotes_1MPath;
%%       基础因子（5分钟线）存放文件夹
DailyQuotes_5MPath=[Path,'BackTestDataBase/DataBase/AllData/QuoteFactor_mat/DailyQuotes_5M'];
if ~isdir(DailyQuotes_5MPath)
    mkdir(DailyQuotes_5MPath)
end
ret.DailyQuotes_5MPath=DailyQuotes_5MPath;
%%       基础因子（10分钟线）存放文件夹
DailyQuotes_10MPath=[Path,'BackTestDataBase/DataBase/AllData/QuoteFactor_mat/DailyQuotes_10M'];
if ~isdir(DailyQuotes_10MPath)
    mkdir(DailyQuotes_10MPath)
end
ret.DailyQuotes_10MPath=DailyQuotes_10MPath;
%%       基础因子（15分钟线）存放文件夹
DailyQuotes_15MPath=[Path,'BackTestDataBase/DataBase/AllData/QuoteFactor_mat/DailyQuotes_15M'];
if ~isdir(DailyQuotes_15MPath)
    mkdir(DailyQuotes_15MPath)
end
ret.DailyQuotes_15MPath=DailyQuotes_15MPath;
%%       基础因子（30分钟线）存放文件夹
DailyQuotes_30MPath=[Path,'BackTestDataBase/DataBase/AllData/QuoteFactor_mat/DailyQuotes_30M'];
if ~isdir(DailyQuotes_30MPath)
    mkdir(DailyQuotes_30MPath)
end
ret.DailyQuotes_30MPath=DailyQuotes_30MPath;
%%       基础因子（60分钟线）存放文件夹
DailyQuotes_60MPath=[Path,'BackTestDataBase/DataBase/AllData/QuoteFactor_mat/DailyQuotes_60M'];
if ~isdir(DailyQuotes_60MPath)
    mkdir(DailyQuotes_60MPath)
end
ret.DailyQuotes_60MPath=DailyQuotes_60MPath;