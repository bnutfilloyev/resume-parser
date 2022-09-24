from loader import dp
from aiogram import types

from pyresparser import ResumeParser

template_message = "<b>Full Name</b>: {name}\n" \
                   "<b>Email</b>: {email}\n" \
                   "<b>Mobile Number</b>: {mobile_number}\n" \
                   "<b>Skills</b>: {skills}\n" \
                   "<b>College Name</b>: {college_name}\n" \
                   "<b>Degree</b>: {degree}\n" \
                   "<b>Designation</b>: {designation}\n" \
                   "<b>Experience</b>: {experience}\n" \
                   "<b>Company</b>: {company_names}\n"


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def resume(message: types.Message):
    file = await message.document.download()
    data = ResumeParser(file.name).get_extracted_data()
    await message.answer(template_message.format(**data))
