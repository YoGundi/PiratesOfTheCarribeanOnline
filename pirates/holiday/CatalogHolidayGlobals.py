# File: C (Python 2.4)

from pirates.ai.HolidayDates import *

class ConfigIds:
    CAT1 = 1
    CAT2 = 2
    CAT3 = 3
    CAT4 = 4
    CAT5 = 5
    CAT6 = 6
    CAT7 = 7
    CAT8 = 8
    CAT9 = 9
    CAT10 = 10
    CAT11 = 11
    CAT12 = 12
    CAT13 = 13
    CAT14 = 14
    Outfit_3 = 97
    Outfit_2 = 98
    Outfit_1 = 99

CatalogHolidayConfigs = {
    ConfigIds.CAT1: {
        'id': ConfigIds.CAT1,
        'name': 'CAT1',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.NOVEMBER, 1, 0, 0, 0),
            (Month.DECEMBER, 31, 23, 59, 0)]) },
    ConfigIds.CAT2: {
        'id': ConfigIds.CAT2,
        'name': 'CAT2',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.DECEMBER, 1, 0, 0, 0),
            (Month.DECEMBER, 31, 23, 59, 0),
            (Month.JANUARY, 1, 0, 0, 0),
            (Month.JANUARY, 31, 23, 59, 0)]) },
    ConfigIds.CAT3: {
        'id': ConfigIds.CAT3,
        'name': 'CAT3',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.JANUARY, 1, 0, 0, 0),
            (Month.FEBRUARY, 28, 23, 59, 0)]) },
    ConfigIds.CAT4: {
        'id': ConfigIds.CAT4,
        'name': 'CAT4',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.FEBRUARY, 1, 0, 0, 0),
            (Month.MARCH, 31, 23, 59, 0)]) },
    ConfigIds.CAT5: {
        'id': ConfigIds.CAT5,
        'name': 'CAT5',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.MARCH, 1, 0, 0, 0),
            (Month.APRIL, 30, 23, 59, 0)]) },
    ConfigIds.CAT6: {
        'id': ConfigIds.CAT6,
        'name': 'CAT6',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.APRIL, 1, 0, 0, 0),
            (Month.MAY, 31, 23, 59, 0)]) },
    ConfigIds.CAT7: {
        'id': ConfigIds.CAT7,
        'name': 'CAT7',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.MAY, 1, 0, 0, 0),
            (Month.JUNE, 30, 23, 59, 0)]) },
    ConfigIds.CAT8: {
        'id': ConfigIds.CAT8,
        'name': 'CAT8',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.JUNE, 1, 0, 0, 0),
            (Month.JULY, 31, 23, 59, 0)]) },
    ConfigIds.CAT9: {
        'id': ConfigIds.CAT9,
        'name': 'CAT9',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.JULY, 1, 0, 0, 0),
            (Month.AUGUST, 31, 23, 59, 0)]) },
    ConfigIds.CAT10: {
        'id': ConfigIds.CAT10,
        'name': 'CAT10',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.AUGUST, 1, 0, 0, 0),
            (Month.SEPTEMBER, 30, 23, 59, 0)]) },
    ConfigIds.CAT11: {
        'id': ConfigIds.CAT11,
        'name': 'CAT11',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.SEPTEMBER, 1, 0, 0, 0),
            (Month.OCTOBER, 31, 23, 59, 0)]) },
    ConfigIds.CAT12: {
        'id': ConfigIds.CAT12,
        'name': 'CAT12',
        'dates': HolidayDates(HolidayDates.TYPE_YEARLY, [
            (Month.OCTOBER, 1, 0, 0, 0),
            (Month.NOVEMBER, 30, 23, 59, 0)]) },
    ConfigIds.Outfit_3: {
        'id': ConfigIds.Outfit_3,
        'name': 'Catalog (Outfit 3)' },
    ConfigIds.Outfit_2: {
        'id': ConfigIds.Outfit_2,
        'name': 'Catalog (Outfit 2)' },
    ConfigIds.Outfit_1: {
        'id': ConfigIds.Outfit_1,
        'name': 'Catalog (Outfit 1)' } }
