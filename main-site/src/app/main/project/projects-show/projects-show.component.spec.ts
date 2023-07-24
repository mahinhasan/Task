import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjectsShowComponent } from './projects-show.component';

describe('ProjectsShowComponent', () => {
  let component: ProjectsShowComponent;
  let fixture: ComponentFixture<ProjectsShowComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProjectsShowComponent]
    });
    fixture = TestBed.createComponent(ProjectsShowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
