import { parsePhoneNumber } from 'libphonenumber-js';

import Specialties from './Specialties';
import AdvocateType from './types';

const TableCell = (props) => (<td className="p-2" {...props} />);

const TableRow = (
  { advocate: {
    city,
    degree,
    firstName,
    lastName,
    phoneNumber,
    specialties,
    yearsOfExperience,
  } }:
  { advocate: AdvocateType; }
) => (
  <tr>
    <TableCell>{firstName}</TableCell>
    <TableCell>{lastName}</TableCell>
    <TableCell>{city}</TableCell>
    <TableCell>{degree}</TableCell>
    <TableCell>
      <Specialties specialties={specialties} />
    </TableCell>
    <TableCell>{yearsOfExperience}</TableCell>
    <TableCell>
        {parsePhoneNumber(`${phoneNumber}`, 'US').formatNational()}
    </TableCell>
  </tr>
);

export default TableRow;
