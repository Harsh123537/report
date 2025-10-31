
BULK INSERT GQDP_STAGE.dbo.[DAT_STG_CITI_COMPLAINT_CONTACT_1.2]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Complaint Contact-1_2_unicode.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );


select * from [dbo].[DAT_STG_CITI_COMPLAINT_CONTACT_1.1]
select * from [dbo].[DAT_STG_CITI_COMPLAINT_CONTACT_21]  where [pr_id]='2708879'
select * into [dbo].[DAT_STG_CITI_COMPLAINT_CONTACT_43] from [dbo].[DAT_STG_CITI_COMPLAINT_CONTACT_36]
--truncate table [dbo].[DAT_STG_CITI_COMPLAINT_CONTACT_27]

select * from [dbo].[DAT_STG_CITI_COMPLAINT_record_7]

BULK INSERT GQDP_STAGE.dbo.[DAT_STG_CITI_COMPLAINT_RECORD_43]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch36_43_CITI_Record Types to unicode\Complaint Record_43.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_COMPLAINT_RECORD_43] from [dbo].[DAT_STG_CITI_COMPLAINT_RECORD_36]
--truncate table [dbo].[DAT_STG_CITI_COMPLAINT_RECORD_36]
select count(*)  from [dbo].[DAT_STG_CITI_COMPLAINT_RECORD]  where [PR_ID] in 
(select [PR_ID] from [dbo].[DAT_STG_CITI_COMPLAINT_RECORD_43])



BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_COMPLAINT_SAMPLE_TRACKING_43]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch36_43_CITI_Record Types to unicode\Complaint Sample Tracking_43.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_COMPLAINT_SAMPLE_TRACKING_43] from [dbo].[DAT_STG_CITI_COMPLAINT_SAMPLE_TRACKING_36]
--truncate table [dbo].[DAT_STG_CITI_COMPLAINT_SAMPLE_TRACKING_36]

select * from   [dbo].[DAT_STG_CITI_COMPLAINT_SAMPLE_TRACKING_38] 


BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_FCI_43]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch36_43_CITI_Record Types to unicode\Full Complaint Investigation_43.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_FCI_43] from [dbo].[DAT_STG_CITI_FCI_36]
--truncate table [dbo].[DAT_STG_CITI_FCI_36]
select * from [dbo].[DAT_STG_CITI_FCI_43]

BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_INTERIM_REPORT_FCI_31]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch21_35_CITI_Record Types to unicode\Interim Report (FCI)_31.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_INTERIM_REPORT_FCI_34] from [DAT_STG_CITI_INTERIM_REPORT_FCI_27]
--truncate table [dbo].[DAT_STG_CITI_INTERIM_REPORT_FCI_27]
select * from [dbo].[DAT_STG_CITI_INTERIM_REPORT_FCI_18]


BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_OFFLINE_INVESTIGATION_43]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch36_43_CITI_Record Types to unicode\Offline Contractor Investigation_43.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_OFFLINE_INVESTIGATION_43] from [dbo].[DAT_STG_CITI_OFFLINE_INVESTIGATION_36]
--truncate table [DAT_STG_CITI_OFFLINE_INVESTIGATION_36]
select * from [dbo].[DAT_STG_CITI_OFFLINE_INVESTIGATION_43]

BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_REPORTER_43]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch36_43_CITI_Record Types to unicode\Reporter_43.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_REPORTER_43] from [dbo].[DAT_STG_CITI_REPORTER_36]
--truncate table [dbo].[DAT_STG_CITI_REPORTER_40]
select * from [dbo].[DAT_STG_CITI_REPORTER_40]

BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_SOURCE_DOC_CORRESPONDANCE_42]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch36_43_CITI_Record Types to unicode\Source Documents Correspondence_42.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_SOURCE_DOC_CORRESPONDANCE_43] from [DAT_STG_CITI_SOURCE_DOC_CORRESPONDANCE_36]
--truncate table [DAT_STG_CITI_SOURCE_DOC_CORRESPONDANCE_36]
select * from [DAT_STG_CITI_SOURCE_DOC_CORRESPONDANCE_43]


BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_ACTION_ITEM_5]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Action Item (CC)_5.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_ACTION_ITEM_16] from [DAT_STG_CITI_ACTION_ITEM_5]
--truncate table [DAT_STG_CITI_ACTION_ITEM_25]
select * from [DAT_STG_CITI_ACTION_ITEM_5]

BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_NOTIFICATION_MANAGEMENT_16]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch11_20_CITI_Record Types to unicode\Notification to Management (FCI)_16.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );

select * into [dbo].[DAT_STG_CITI_NOTIFICATION_MANAGEMENT_16] from [DAT_STG_CITI_NOTIFICATION_MANAGEMENT_28]
--truncate table [DAT_STG_CITI_NOTIFICATION_MANAGEMENT_16]
select * from [DAT_STG_CITI_NOTIFICATION_MANAGEMENT_16]


BULK INSERT GQDP_STAGE.[dbo].[DAT_STG_CITI_SUMMARY_INVESTIGATION_40]
   FROM '\\w0btws002\Deployment\SandBox\Data Archival\Batch36_43_CITI_Record Types to unicode\Summary Investigation_40.txt'
   WITH
     (
         FIRSTROW = 2
    ,FIELDTERMINATOR = '¦'
         , ROWTERMINATOR = '\n'
              , DATAFILETYPE = 'widechar'
      );
