import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.main import Book


class SerializeProcessor(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JSONSerializeProcessor(SerializeProcessor):
    def serialize(self, book: Book) -> None:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializeProcessor(SerializeProcessor):
    def serialize(self, book: Book) -> None:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
