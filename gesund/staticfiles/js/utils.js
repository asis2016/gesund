/**
 * Get today date.
 * */
const get_today = () => {
    let fullDate = new Date();
    let twoDigitMonth = ((fullDate.getMonth().length + 1) === 1) ? (fullDate.getMonth() + 1) : '0' + (fullDate.getMonth() + 1);
    let datestamp = fullDate.getFullYear() + "-" + twoDigitMonth + "-" + fullDate.getDate();
    return datestamp;
}
